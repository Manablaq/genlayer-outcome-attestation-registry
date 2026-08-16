# API Manifest

## Contract

`OutcomeAttestationRegistry`

## Write Methods

```python
request_attestation(subject: str, claim: str, evidence_uri: str, criteria: str, ttl_seconds: u256) -> u256
resolve_attestation(request_id: u256) -> None
```

`request_attestation` captures the complete evidence and criteria snapshot. `resolve_attestation` independently fetches and evaluates this immutable snapshot on every validator, then applies strict equality to the complete canonical result before storage writes.

## View Methods

```python
get_attestation(request_id: u256) -> Attestation
get_latest_by_fingerprint(subject: str, claim: str, evidence_uri: str, criteria: str) -> u256
is_attested_true(request_id: u256, min_confidence: u32) -> bool
is_attested_false(request_id: u256, min_confidence: u32) -> bool
is_fresh(request_id: u256) -> bool
```

`is_attested_true` and `is_attested_false` authorize only fresh records with `consensus_bound = true` and the exact corresponding canonical result.

## Result Codes

```text
0 = unknown
1 = true
2 = false
3 = inconclusive
4 = error
```

## Attestation

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
consensus_bound: bool
created_at: u256
resolved_at: u256
expires_at: u256
resolver: Address
```
