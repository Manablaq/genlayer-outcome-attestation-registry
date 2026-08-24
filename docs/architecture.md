# Architecture

```text
canonical evidence policy
  -> SHA-256 specification fingerprint
  -> independent full-body fetch and SHA-256 verification
  -> freshness and minimum-source policy
  -> strict semantic consensus
  -> immutable attestation
  -> fingerprint-bound consumer view
```

## Deterministic Request Identity

The request specification is a canonical JSON array containing the claim,
source URIs, registered content hashes, authorities, version, semantic criteria,
freshness policy, corroboration threshold, and attestation TTL. SHA-256 of that
encoding is the request fingerprint. JSON escaping makes the encoding
unambiguous; embedded separators cannot alias another request.

## Evidence Integrity

`_evaluate_attestation_snapshot` is the only nondeterministic boundary. Every
validator fetches the complete response body, computes SHA-256 before prompt
truncation, and compares it with the registered commitment. A supplied
corroborating source is verified independently. Integrity flags, full hashes,
source count, and semantic result are all included in strict equality.

No attestation is stored if a fetch fails, a body exceeds the explicit limit, a
hash differs, or the minimum-source policy is unsatisfied.

## Freshness

The request records when the evidence was observed and the maximum permitted
evidence age. Both are checked at request time and again immediately before
consensus. Requests also have a fixed 24-hour resolution window. Successful
attestation expiry begins at `resolved_at`, not request creation.

Consumers provide both an expected fingerprint and their own maximum age. The
consumer views require exact fingerprint equality, `content_verified`,
`consensus_bound`, unexpired state, and resolution age within that limit.
