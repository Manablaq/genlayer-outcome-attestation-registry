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

The hardened v2.1 source is pinned at commit
`60eed18e3861d650bad9895e5b43b277404159a9`. A final fresh deployment and the
live regression links required by `STUDIO_BRADBURY_TEST_PLAN.md` must be
recorded before resubmission. Candidate address `0x981C81...` and historical
address `0x78C17...` are not the final hardened release.
