# Outcome Attestation Registry

`OutcomeAttestationRegistry` is a reusable GenLayer Intelligent Contract for
hash-pinned, freshness-bound attestations over authoritative public evidence.

```text
expected evidence policy -> independent fetch and full-content verification
                         -> strict semantic consensus -> bound attestation
```

> **Release status:** the hardened source is complete, locally verified, and
> deployed on Bradbury at
> `0x981C81A7b532Ca062a1443EB43cd294d8E6d6558`. Live security regressions and
> transaction finalization remain required before resubmission. The previous
> Bradbury deployment at
> `0x78C17d55FB0eA3d768527793749e1AC878b0572C` does not contain these fixes and
> is historical only.

## Security Properties

- **Unambiguous identity.** The complete canonical evidence policy is encoded
  as JSON and SHA-256 hashed. User-controlled separators cannot collide.
- **Immutable evidence commitment.** Validators hash the complete fetched body
  and must match the registered SHA-256 before an attestation can be stored.
- **Explicit authority and version.** Each source records its authority and
  evidence version inside the bound fingerprint.
- **Freshness at two layers.** Evidence observation age is enforced before
  resolution; consumers also set a maximum age measured from `resolved_at`.
- **Optional corroboration.** Requests may require two different HTTPS sources
  from different named authorities. Both content commitments must match.
- **Claim-bound consumption.** Consequential views require the consumer's
  expected fingerprint. A true attestation for another claim cannot be
  substituted by request ID.
- **One nondeterministic boundary.** Web and LLM calls occur only inside the
  function passed to `gl.eq_principle.strict_eq`; storage changes happen after
  integrity and schema validation.

## Core API

```python
request_attestation(
    subject,
    claim,
    primary_evidence_uri,
    primary_evidence_sha256,
    primary_authority,
    corroborating_evidence_uri,
    corroborating_evidence_sha256,
    corroborating_authority,
    evidence_version,
    criteria,
    evidence_observed_at,
    max_evidence_age_seconds,
    minimum_sources,
    ttl_seconds,
) -> u256

resolve_attestation(request_id) -> None
compute_fingerprint(...) -> str
get_request(request_id) -> AttestationRequest
get_attestation(request_id) -> Attestation
get_latest_by_fingerprint(fingerprint) -> u256
is_attested_true_for(request_id, expected_fingerprint, consumer_max_age_seconds) -> bool
is_attested_false_for(request_id, expected_fingerprint, consumer_max_age_seconds) -> bool
is_fresh_for(request_id, expected_fingerprint, consumer_max_age_seconds) -> bool
```

See [API_MANIFEST.md](API_MANIFEST.md) for the complete field reference and
[examples/consumer_contract.py](examples/consumer_contract.py) for the safe
integration pattern.

## Result Codes

```text
0 unknown
1 true
2 false
3 inconclusive
4 error
```

There is no model-controlled confidence score. Consequential authorization is
based on the exact canonical result, verified evidence commitments, consensus
binding, expected fingerprint, attestation expiry, and consumer-selected age.

## Verification

```bash
python3 -m unittest discover -s tests -v
python3 -m py_compile contracts/*.py studio_bradbury/*.py examples/*.py
genvm-lint check contracts/outcome_attestation_registry.py --json
cmp contracts/outcome_attestation_registry.py \
    studio_bradbury/outcome_attestation_registry.py
git diff --check
```

The 13-test suite includes behavioral regressions for the original delimiter collision,
content mutation beyond the old 256-character prefix, hash mismatch rejection,
two-source corroboration, resolution-time freshness, and consumer binding.
The official `genvm-linter` 0.10.0 gate passes both AST linting and SDK semantic
validation (9 public methods: 7 views and 2 writes).

## Deployment Gate

Do not cite a contract address as the hardened release until all steps in
[STUDIO_BRADBURY_TEST_PLAN.md](STUDIO_BRADBURY_TEST_PLAN.md) pass against a
fresh instance. Record the address, deployment transaction, exact source commit,
source SHA-256, and all regression transactions in
[TEST_LOG_BRADBURY.md](TEST_LOG_BRADBURY.md).

## Repository Layout

```text
contracts/outcome_attestation_registry.py        primary source
studio_bradbury/outcome_attestation_registry.py  byte-identical Studio source
tests/test_consensus_design.py                    security regressions
examples/                                         bound consumer and JS usage
docs/                                             architecture and testing notes
```
