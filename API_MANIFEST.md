# API Manifest

## Contract

`OutcomeAttestationRegistry`

## Write Methods

```python
request_attestation(
    subject: str,
    claim: str,
    primary_evidence_uri: str,
    primary_evidence_sha256: str,
    primary_authority: str,
    corroborating_evidence_uri: str,
    corroborating_evidence_sha256: str,
    corroborating_authority: str,
    evidence_version: str,
    criteria: str,
    evidence_observed_at: u256,
    max_evidence_age_seconds: u256,
    minimum_sources: u32,
    ttl_seconds: u256,
) -> u256

resolve_attestation(request_id: u256) -> None
```

The request commits to the complete evidence policy. Each validator hashes the
entire fetched response and strict equality binds both the decision and observed
content hashes. Resolution aborts if any registered hash or minimum-source rule
is not satisfied.

## View Methods

```python
get_request(request_id: u256) -> AttestationRequest
get_attestation(request_id: u256) -> Attestation
get_latest_by_fingerprint(fingerprint: str) -> u256
compute_fingerprint(...) -> str
is_attested_true_for(
    request_id: u256,
    expected_fingerprint: str,
    consumer_max_age_seconds: u256,
) -> bool
is_attested_false_for(
    request_id: u256,
    expected_fingerprint: str,
    consumer_max_age_seconds: u256,
) -> bool
is_fresh_for(
    request_id: u256,
    expected_fingerprint: str,
    consumer_max_age_seconds: u256,
) -> bool
```

There is intentionally no request-ID-only authorization method. Consequential
consumers must store their expected fingerprint and pass it to the bound view.

## Result Codes

```text
0 = unknown
1 = true
2 = false
3 = inconclusive
4 = error
```

## Attestation Security Fields

```python
fingerprint: str                       # SHA-256 of canonical evidence policy
primary_evidence_sha256: str           # registered commitment
corroborating_evidence_sha256: str     # optional registered commitment
primary_content_sha256: str            # validator-observed full-body hash
corroborating_content_sha256: str      # optional observed full-body hash
verified_source_count: u32
content_verified: bool
evidence_observed_at: u256
max_evidence_age_seconds: u256
resolved_at: u256
expires_at: u256                       # resolved_at + requested TTL
consensus_bound: bool
```
