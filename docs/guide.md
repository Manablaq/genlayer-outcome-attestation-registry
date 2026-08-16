# Outcome Attestation Registry Guide

## Lifecycle

1. Call `request_attestation` with a subject, claim, public evidence URI, criteria, and expiry.
2. The contract stores an immutable request snapshot and a canonical fingerprint.
3. Call `resolve_attestation`.
4. Every validator independently fetches the registered evidence and applies the stored criteria.
5. Strict equality accepts a full canonical result before the contract writes it.
6. Consumers use `is_attested_true`, `is_attested_false`, or `is_fresh`.

## Independent Validation

Validators do not merely inspect a leader payload. They repeat the evidence fetch and criteria evaluation. The outcome, canonical confidence, reason, summary, and evidence digest must all match under strict equality. Confidence is derived by result category, not supplied by an untrusted model.

## Consumer Safety

`is_attested_true` and `is_attested_false` require `consensus_bound = true`, freshness, the exact stored result, and the requested confidence threshold. A schema-valid but contradictory output cannot change downstream behavior.

## Evidence Sources

Use stable public HTTPS sources with a precise, binary policy. GitHub API and document URLs are supported through the same generic resolver; there is no special GitHub execution path.
