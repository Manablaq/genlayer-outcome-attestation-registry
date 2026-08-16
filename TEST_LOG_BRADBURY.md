# Bradbury Test Log

## Historical Result

The tests for `0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63` are historical only. That version included a GitHub-specific resolver structure that is not part of the corrected source.

## Corrected Test Requirements

Record the fresh accepted deployment transaction and then demonstrate:

```text
request_attestation
resolve_attestation
get_attestation with consensus_bound: true
is_attested_true or is_attested_false at canonical confidence
```

The corrected resolver performs no storage writes inside non-deterministic evaluation and requires validators to independently verify all consequential outputs before strict equality permits storage.
