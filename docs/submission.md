# Submission Summary

`OutcomeAttestationRegistry` is a reusable primitive for attestations over
authoritative, hash-pinned public evidence.

Each request binds the claim to HTTPS source URIs, full SHA-256 commitments,
named authorities, an evidence version, observation-time freshness policy,
semantic criteria, optional independent corroboration, and attestation TTL.
Every validator independently fetches and hashes the complete evidence body.
Strict equality binds the observed hashes, integrity result, source count, and
canonical decision before storage.

Downstream authorization is specification-bound: consumers must provide the
exact expected SHA-256 fingerprint and their own maximum attestation age. An
unrelated true request ID cannot authorize another claim.

## Resubmission Evidence

The hardened source is deployed on Bradbury at
`0xce871c6045e7B1B0c3F73652BFaeD02eB06A8252`. The exact source revision,
deployment transaction, and completed live regression are recorded in
`DEPLOYMENT_BRADBURY.md` and `TEST_LOG_BRADBURY.md`. Previous deployments are
historical evidence only.
