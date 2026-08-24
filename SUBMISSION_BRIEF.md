# Submission Brief

## Outcome Attestation Registry

A reusable GenLayer primitive that turns authoritative, versioned and
hash-pinned public evidence into specification-bound attestations.

## Security Boundary

- SHA-256 of canonical JSON identifies the complete request specification.
- Validators hash each complete fetched body and require the registered
  commitment before storage.
- Requests encode authority, version, observation time, maximum evidence age,
  and a one- or two-source corroboration policy.
- Strict equality binds the result, observed hashes, integrity flag and verified
  source count.
- Attestation lifetime begins at successful resolution.
- Consumers must match the exact expected fingerprint and select their own
  maximum acceptable resolution age.

## Evidence Status

The repository is prepared for a fresh deployment. Do not submit the historical
`0x78C17...` address as the hardened release. Add the new address, accepted
deployment transaction, source commit, source SHA-256, and completed regression
links here only after executing `STUDIO_BRADBURY_TEST_PLAN.md`.
