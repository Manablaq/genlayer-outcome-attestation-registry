# Outcome Attestation Registry Guide

## Lifecycle

1. Fetch the authoritative evidence bytes and compute their SHA-256.
2. Select the authority, immutable version label, observation time, maximum
   evidence age, semantic criteria, and attestation TTL.
3. Optionally add a second HTTPS source from an independent authority and set
   `minimum_sources` to `2`.
4. Call `compute_fingerprint` and store that fingerprint in the consuming
   contract or action configuration.
5. Call `request_attestation` with the exact same specification.
6. Call `resolve_attestation` within 24 hours and before the evidence becomes
   stale.
7. Validators independently fetch, hash, and evaluate the registered sources.
8. Consumers call `is_attested_true_for`, `is_attested_false_for`, or
   `is_fresh_for` with their stored expected fingerprint and maximum age.

## Source Selection

Use authoritative HTTPS endpoints. Prefer immutable URLs, signed records,
versioned APIs, or commit-addressed files. The SHA-256 commitment remains
mandatory even when the URL is immutable. If one source is not sufficient for
the use case, require two authorities rather than placing two URLs behind the
same publisher.

## Safe Consumer Pattern

Never accept an arbitrary expected fingerprint from the same caller who
supplies `request_id`. The consumer must store the expected fingerprint when
its protected action is configured. See
[`examples/consumer_contract.py`](../examples/consumer_contract.py).

## Limits

- Request resolution window: 24 hours
- Attestation TTL: 5 minutes to 30 days; zero selects 7 days
- Evidence observation age policy: 1 minute to 30 days
- Fetched body: 12,000 bytes per source, ensuring the complete accepted body is
  available to semantic evaluation as well as full-body hashing
