# Studio Bradbury Test Plan

## 1. Local Verification

Run the commands in `docs/testing.md`. Confirm 14 tests pass and the primary and
Studio sources are byte-identical.

## 2. Prepare Evidence

Select a stable authoritative HTTPS record no larger than 12,000 bytes. Capture the
exact response bytes and calculate:

```bash
curl -sS https://authority.example/immutable-record -o /tmp/oar-primary.bin
shasum -a 256 /tmp/oar-primary.bin
date +%s
```

For the corroborated path, repeat with a distinct URI controlled by a different
authority. Do not normalize, decode, or reserialize the bytes before hashing.

## 3. Deploy

```bash
genlayer account unlock --account worker
genlayer deploy --contract studio_bradbury/outcome_attestation_registry.py
```

Record the address, deployment transaction, exact commit, file size, and source
SHA-256 in `DEPLOYMENT_BRADBURY.md`.

## 4. Happy Path

1. Call `compute_fingerprint` for the complete evidence specification.
2. Call `request_attestation` with the identical arguments.
3. Call `resolve_attestation(request_id)`.
4. Confirm the stored fingerprint and content hashes match the registered
   values, with `content_verified: true` and `consensus_bound: true`.
5. Call the matching `is_attested_true_for` or `is_attested_false_for` using the
   computed fingerprint and an explicit consumer maximum age.

## 5. Security Regressions

1. **Substitution:** change one character of the expected fingerprint; the
   consumer view must return `false`.
2. **Integrity mismatch:** create a request with an incorrect hash and attempt
   resolution; it must fail without storing an attestation.
3. **Corroboration:** create a two-authority request with `minimum_sources = 2`;
   resolution must store both exact hashes and `verified_source_count: 2`.
4. **Freshness:** use an observation timestamp older than its maximum age; the
   request must fail.

## 6. Finalization

Wait for each transaction to finalize. Update `TEST_LOG_BRADBURY.md` with direct
Explorer links and exact read outputs before resubmission.
