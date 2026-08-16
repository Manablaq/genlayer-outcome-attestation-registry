# Bradbury Testing Guide

Follow `STUDIO_BRADBURY_TEST_PLAN.md` after a fresh deployment.

For resubmission capture:

1. Accepted deployment transaction for the byte-identical Studio source.
2. `request_attestation` inputs and returned request id.
3. Accepted `resolve_attestation` transaction.
4. `get_attestation` output showing a canonical result, matching canonical confidence, evidence digest, and `consensus_bound: true`.
5. The matching `is_attested_true` or `is_attested_false` result at the canonical confidence threshold.

`tests/test_consensus_design.py` asserts that there is no special GitHub resolver, no `run_nondet_unsafe`, no nested resolver lambda, and no consumer authorization without consensus binding. It also checks the Studio and primary contract sources remain identical.
