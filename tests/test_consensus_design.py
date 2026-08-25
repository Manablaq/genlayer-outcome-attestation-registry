"""Behavioral and structural regressions for the hardened security boundary."""

import ast
import hashlib
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "contracts" / "outcome_attestation_registry.py").read_text()
STUDIO_SOURCE = (ROOT / "studio_bradbury" / "outcome_attestation_registry.py").read_text()


def _load_contract_helpers():
    selected = {
        "_canonical",
        "_sha256_hex",
        "_normalize_sha256",
        "_is_sha256_hex",
        "_spec_fingerprint",
        "_fresh_at",
        "_coerce_json_object",
        "_canonical_reason_code",
        "_canonical_summary",
        "_normalize_resolution",
        "_is_valid_resolution",
    }
    tree = ast.parse(SOURCE)
    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name in selected
    ]
    namespace = {"hashlib": hashlib, "json": json, "re": re}
    exec(
        compile(ast.Module(body=functions, type_ignores=[]), "contract_helpers", "exec"),
        namespace,
    )
    return namespace


HELPERS = _load_contract_helpers()


def _spec(**overrides):
    values = {
        "subject": "Official result",
        "claim": "The proposal passed.",
        "primary_evidence_uri": "https://authority.example/result/v1.json",
        "primary_evidence_sha256": "a" * 64,
        "primary_authority": "Official Authority",
        "corroborating_evidence_uri": "",
        "corroborating_evidence_sha256": "",
        "corroborating_authority": "",
        "evidence_version": "v1",
        "criteria": "Return true only if the result explicitly says passed.",
        "evidence_observed_at": 1_700_000_000,
        "max_evidence_age_seconds": 86_400,
        "minimum_sources": 1,
        "ttl_seconds": 3_600,
    }
    values.update(overrides)
    return values


class OutcomeAttestationConsensusTests(unittest.TestCase):
    def test_nondeterminism_is_not_in_contract_write_methods(self):
        tree = ast.parse(SOURCE)
        contract = next(
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef)
            and node.name == "OutcomeAttestationRegistry"
        )
        for method in contract.body:
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                implementation = ast.get_source_segment(SOURCE, method) or ""
                self.assertNotIn("gl.nondet", implementation, method.name)

    def test_studio_source_matches_deployable_source(self):
        self.assertEqual(SOURCE, STUDIO_SOURCE)

    def test_validators_bind_full_content_hashes(self):
        self.assertIn("gl.nondet.web.get", SOURCE)
        self.assertIn("_sha256_hex(body)", SOURCE)
        self.assertIn("gl.eq_principle.strict_eq(evaluate_attestation)", SOURCE)
        self.assertIn('if not agreed["integrity_ok"]', SOURCE)
        self.assertNotIn("gl.vm.run_nondet_unsafe", SOURCE)

    def test_delimiter_injection_no_longer_collides(self):
        fingerprint = HELPERS["_spec_fingerprint"]
        first = _spec(subject="a|b", claim="c", primary_evidence_uri="d")
        second = _spec(subject="a", claim="b", primary_evidence_uri="c|d")
        self.assertNotEqual(fingerprint(**first), fingerprint(**second))

    def test_exact_spec_has_stable_fingerprint(self):
        fingerprint = HELPERS["_spec_fingerprint"]
        first = _spec(subject=" Official Result ", primary_evidence_sha256="A" * 64)
        second = _spec(subject="Official Result", primary_evidence_sha256="a" * 64)
        self.assertEqual(fingerprint(**first), fingerprint(**second))

    def test_case_sensitive_policy_text_does_not_alias(self):
        fingerprint = HELPERS["_spec_fingerprint"]
        self.assertNotEqual(
            fingerprint(**_spec(criteria="Require status ID A")),
            fingerprint(**_spec(criteria="Require status ID a")),
        )

    def test_full_content_hash_detects_changes_after_old_prefix(self):
        sha256_hex = HELPERS["_sha256_hex"]
        prefix = b"same" * 64
        self.assertNotEqual(
            sha256_hex(prefix + b"first authoritative outcome"),
            sha256_hex(prefix + b"manipulated authoritative outcome"),
        )

    def test_hash_mismatch_cannot_be_stored_as_true(self):
        normalize = HELPERS["_normalize_resolution"]
        snapshot = _spec()
        primary = {
            "ok": True,
            "body": b"changed",
            "sha256": "b" * 64,
            "error": "",
        }
        empty = {"ok": True, "body": b"", "sha256": "", "error": ""}
        result = normalize({"result": "true"}, snapshot, primary, empty)
        self.assertFalse(result["integrity_ok"])
        self.assertEqual(result["result"], "error")

    def test_two_source_policy_requires_both_hashes(self):
        normalize = HELPERS["_normalize_resolution"]
        snapshot = _spec(
            corroborating_evidence_uri="https://second.example/v1.json",
            corroborating_evidence_sha256="b" * 64,
            corroborating_authority="Independent Authority",
            minimum_sources=2,
        )
        primary = {"ok": True, "body": b"", "sha256": "a" * 64, "error": ""}
        bad_secondary = {
            "ok": True,
            "body": b"",
            "sha256": "c" * 64,
            "error": "",
        }
        result = normalize({"result": "true"}, snapshot, primary, bad_secondary)
        self.assertFalse(result["integrity_ok"])
        self.assertEqual(result["verified_source_count"], 1)
        self.assertEqual(result["result"], "error")

    def test_freshness_is_measured_from_resolution(self):
        fresh_at = HELPERS["_fresh_at"]
        self.assertTrue(fresh_at(1_000, 2_000, 1_300, 300))
        self.assertFalse(fresh_at(1_000, 2_000, 1_301, 300))
        self.assertFalse(fresh_at(1_000, 1_300, 1_300, 300))
        self.assertFalse(fresh_at(1_000, 2_000, 999, 300))

    def test_consumers_must_supply_expected_fingerprint(self):
        self.assertIn("def is_attested_true_for(", SOURCE)
        self.assertIn("def is_attested_false_for(", SOURCE)
        self.assertIn("expected_fingerprint: str", SOURCE)
        self.assertIn("attestation.fingerprint ==", SOURCE)
        self.assertNotIn("def is_attested_true(", SOURCE)
        self.assertNotIn("def is_attested_false(", SOURCE)

    def test_expired_or_stale_requests_are_rejected_before_consensus(self):
        self.assertIn('raise gl.vm.UserError("request resolution window expired")', SOURCE)
        self.assertIn('raise gl.vm.UserError("evidence became stale before resolution")', SOURCE)
        self.assertIn("expires_at=resolved_at + req.attestation_ttl_seconds", SOURCE)

    def test_request_inputs_have_explicit_bounds(self):
        self.assertIn("MAX_CLAIM_CHARS", SOURCE)
        self.assertIn("MAX_CRITERIA_CHARS", SOURCE)
        self.assertIn("MAX_TTL_SECONDS", SOURCE)
        self.assertIn("MAX_EVIDENCE_AGE_SECONDS", SOURCE)
        self.assertIn("MAX_EVIDENCE_BYTES", SOURCE)

    def test_missing_records_are_checked_before_attribute_access(self):
        self.assertIn("if request_id not in self.requests:", SOURCE)
        self.assertIn("if request_id not in self.attestations:", SOURCE)
        self.assertNotIn("if req.created_at == u256(0):", SOURCE)
        self.assertNotIn("if attestation.created_at == u256(0):", SOURCE)


if __name__ == "__main__":
    unittest.main()
