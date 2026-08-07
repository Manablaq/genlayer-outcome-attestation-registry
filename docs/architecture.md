# Architecture

## Contract Role

`OutcomeAttestationRegistry` is a registry and resolver coordinator.

It does not try to be a full application. Instead, it gives applications a common way to create and consume verified claims.

## Flow

```text
Builder or app
  |
  | request_attestation(...)
  v
AttestationRequest stored by request_id
  |
  | resolve profile
  v
GenLayer nondeterministic evidence fetch
  |
  | consensus accepted
  v
Deterministic normalization and storage
  |
  | view/verifier methods
  v
Consumer contract or frontend
```

## Storage

### AttestationRequest

```python
requester: Address
subject: str
claim: str
evidence_uri: str
criteria: str
fingerprint: str
created_at: u256
expires_at: u256
resolved: bool
```

### Attestation

```python
request_id: u256
requester: Address
subject: str
claim: str
evidence_uri: str
criteria: str
fingerprint: str
result: u32
confidence: u32
reason_code: str
summary: str
evidence_digest: str
created_at: u256
resolved_at: u256
expires_at: u256
resolver: Address
```

## Fingerprint Reuse

The fingerprint is based on canonicalized:

```text
subject
claim
evidence_uri
criteria
```

If a fresh resolved attestation already exists, `request_attestation` returns that existing request id. If there is a fresh unresolved request, it returns the pending id.

This matters because reusable claims should become shared infrastructure rather than repeated work.

## Resolver Design

The contract separates the registry from resolver profiles.

The registry is generic:

```text
request -> resolve -> store -> verify
```

Resolver profiles are domain-specific:

```text
GitHub repository evidence
future: CI status evidence
future: JSON field match evidence
future: document equivalence evidence
future: semantic policy evidence
```

## Why Deterministic Profiles Matter

The Bradbury tests showed that structured API evidence is better handled with deterministic resolver profiles than a generic LLM judgment.

For GitHub repository metadata, the v4 resolver:

1. Fetches the GitHub API response with `gl.nondet.web.get`.
2. Reads `response.body`.
3. Parses JSON.
4. Normalizes stable fields.
5. Applies deterministic checks after consensus.

This avoids unnecessary LLM disagreement for data that can be evaluated directly.

## Consumer API

The contract exposes small verifier methods:

```python
is_attested_true(request_id, min_confidence)
is_attested_false(request_id, min_confidence)
is_fresh(request_id)
```

These methods are what downstream contracts should depend on.

## Architecture Asset

The documentation site includes an architecture diagram at:

```text
site/assets/architecture.svg
```
