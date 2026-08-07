# API Manifest

## Contract

`OutcomeAttestationRegistry`

## Constructor

```python
__init__()
```

No arguments.

## Write Methods

### request_attestation

```python
request_attestation(
    subject: str,
    claim: str,
    evidence_uri: str,
    criteria: str,
    ttl_seconds: u256,
) -> u256
```

Creates an attestation request or returns an existing fresh request/attestation with the same canonical fingerprint.

### resolve_attestation

```python
resolve_attestation(request_id: u256) -> None
```

Fetches evidence, evaluates the claim with an LLM inside a nondeterministic block, validates the structured result, and stores the attestation after consensus.

### resolve_github_repo_attestation

```python
resolve_github_repo_attestation(request_id: u256) -> None
```

Fetches a GitHub repository API response, normalizes stable fields with `strict_eq`, then applies deterministic resolver logic outside the nondeterministic block. Use this profile for GitHub repository existence/metadata attestations.

## View Methods

### get_attestation

```python
get_attestation(request_id: u256) -> Attestation
```

Returns the full resolved attestation. Raises `unknown attestation` if unresolved or missing.

### get_latest_by_fingerprint

```python
get_latest_by_fingerprint(
    subject: str,
    claim: str,
    evidence_uri: str,
    criteria: str,
) -> u256
```

Returns the latest resolved request id for a canonical claim fingerprint, or `0`.

### is_attested_true

```python
is_attested_true(request_id: u256, min_confidence: u32) -> bool
```

Returns `true` only when the attestation is fresh, resolved as true, and confidence meets the threshold.

### is_attested_false

```python
is_attested_false(request_id: u256, min_confidence: u32) -> bool
```

Returns `true` only when the attestation is fresh, resolved as false, and confidence meets the threshold.

### is_fresh

```python
is_fresh(request_id: u256) -> bool
```

Returns `true` when the attestation exists and has not expired.

## Storage Types

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

## Result Codes

```text
0 = unknown
1 = true
2 = false
3 = inconclusive
4 = error
```
