# Testing Guide

## Local Gate

```bash
python3 -m unittest discover -s tests -v
python3 -m py_compile contracts/*.py studio_bradbury/*.py examples/*.py
genvm-lint check contracts/outcome_attestation_registry.py --json
cmp contracts/outcome_attestation_registry.py \
    studio_bradbury/outcome_attestation_registry.py
git diff --check
```

The current suite executes the contract's pure fingerprint, SHA-256, integrity,
corroboration, and freshness helpers and checks the consensus/storage structure.
The official `genvm-linter` 0.10.0 check passes both lint and SDK semantic
validation for the hardened source.

## Required Bradbury Regression

A submission-ready deployment must demonstrate:

1. Accepted fresh deployment from the exact committed Studio source.
2. Request with a full SHA-256 commitment and explicit freshness policy.
3. Successful true or false resolution with `content_verified: true`.
4. `primary_content_sha256` exactly equals the registered hash.
5. Correct expected fingerprint authorizes the matching consumer view.
6. A different expected fingerprint returns `false`.
7. A request with an incorrect content hash cannot store an attestation.
8. For a two-source request, both hashes and `verified_source_count: 2` are
   recorded.
9. A stale evidence observation or expired request is rejected.

Record every transaction and read in `TEST_LOG_BRADBURY.md`. Do not reuse the
historical `0x78C17...` deployment because it predates these guarantees.
