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

The hardened source is deployed at
`0x981C81A7b532Ca062a1443EB43cd294d8E6d6558` by transaction
`0xcaa934bf722f484b6edaaf0629f7f39f7c8a4d9a5deb91fc23df061ee81e0505`.
Do not resubmit until that transaction is finalized and the live regression
links required by `STUDIO_BRADBURY_TEST_PLAN.md` are recorded. The historical
`0x78C17...` address is not the hardened release.
