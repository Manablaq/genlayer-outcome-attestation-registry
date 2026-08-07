# Bradbury Testing Guide

## Active Test Deployment

```text
Network: GenLayer Bradbury Testnet
Contract: 0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
```

## Positive Smoke Test

### 1. Request Attestation

Call:

```text
request_attestation
```

Inputs:

```text
subject:
github.com/genlayerlabs/genlayer-project-boilerplate
```

```text
claim:
The repository exists and is a GenLayer-related project.
```

```text
evidence_uri:
https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
```

```text
criteria:
Return true only if the evidence clearly identifies an existing GitHub repository under genlayerlabs and the repository metadata or description indicates it is related to GenLayer. Return inconclusive if the repository cannot be fetched or the relationship is unclear.
```

```text
ttl_seconds:
604800
```

Known successful request:

```text
request_id: 2
```

### 2. Resolve

Call:

```text
resolve_github_repo_attestation
```

Input:

```text
request_id:
2
```

### 3. Read Attestation

Call:

```text
get_attestation
```

Input:

```text
request_id:
2
```

Observed result:

```text
result: 1
confidence: 9500
reason_code: github_repo_verified
summary: The evidence identifies an existing, usable GitHub repository related to GenLayer.
```

### 4. Verify Consumer API

Call:

```text
is_attested_true
```

Inputs:

```text
request_id:
2
min_confidence:
7000
```

Observed result:

```text
true
```

### 5. Verify Fingerprint Reuse

Call:

```text
get_latest_by_fingerprint
```

Use the same subject, claim, evidence URI, and criteria.

Observed result:

```text
2
```

## Lessons From Testing

The first generic resolver tests returned `UNDETERMINED / DISAGREE / FINISHED_WITH_ERROR`. That led to two improvements:

- structured API claims now use deterministic resolver profiles
- the GitHub resolver reads `response.body` from `gl.nondet.web.get()` instead of assuming a `status_code` field

The successful v4 test demonstrates the intended contract behavior.
