"""Regression checks for the reviewer-required consensus boundary."""

import ast
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "contracts" / "outcome_attestation_registry.py").read_text()
STUDIO_SOURCE = (ROOT / "studio_bradbury" / "outcome_attestation_registry.py").read_text()


class OutcomeAttestationConsensusTests(unittest.TestCase):
    def test_nondeterminism_is_not_in_contract_write_methods(self):
        tree = ast.parse(SOURCE)
        contract = next(
            node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "OutcomeAttestationRegistry"
        )
        for method in contract.body:
            if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                implementation = ast.get_source_segment(SOURCE, method) or ""
                self.assertNotIn("gl.nondet", implementation, method.name)

    def test_studio_source_matches_deployable_source(self):
        self.assertEqual(SOURCE, STUDIO_SOURCE)

    def test_validators_independently_evaluate_registered_evidence(self):
        self.assertIn("def _evaluate_attestation_snapshot(snapshot)", SOURCE)
        self.assertIn("gl.nondet.web.get", SOURCE)
        self.assertIn("gl.nondet.exec_prompt", SOURCE)
        self.assertIn("gl.eq_principle.strict_eq(evaluate_attestation)", SOURCE)
        self.assertNotIn("gl.vm.run_nondet_unsafe", SOURCE)

    def test_consequential_views_require_consensus_binding(self):
        self.assertIn("consensus_bound: bool", SOURCE)
        self.assertIn("and attestation.consensus_bound", SOURCE)
        self.assertIn("evidence_digest=str(agreed[\"evidence_digest\"])[:128]", SOURCE)

    def test_unsafe_github_specific_resolver_is_removed(self):
        self.assertNotIn("resolve_github_repo_attestation", SOURCE)
        self.assertNotIn("_fetch_github_repo_snapshot", SOURCE)
        self.assertNotIn("lambda:", SOURCE)


if __name__ == "__main__":
    unittest.main()
