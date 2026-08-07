# Outcome Attestation Registry

A reusable GenLayer **Intelligent Contract** primitive for creating, resolving, caching, and consuming consensus-backed attestations about external outcomes and structured claims.

The contract is built for GenLayer builders who need a shared adjudication layer instead of reimplementing web access, AI evaluation, result storage, expiry, and verifier methods inside every application contract.

```text
subject + claim + evidence_uri + criteria -> attestation result
```

## Active Deployment

```text
Network:  GenLayer Bradbury Testnet
Contract: 0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
```

Repository:

```text
https://github.com/Manablaq/genlayer-outcome-attestation-registry
```

Documentation site:

```text
docs/index.html
```

## What It Does

`OutcomeAttestationRegistry` lets a builder:

1. Create a structured attestation request.
2. Resolve it with a GenLayer resolver profile.
3. Store the result on-chain.
4. Reuse the result by canonical fingerprint.
5. Expose simple verifier methods for other contracts and frontends.

The registry is intentionally not an app-specific escrow, market, bounty, or reputation contract. It is a reusable Intelligent Contract building block those systems can depend on.

## Why It Is Useful

Many GenLayer applications need to answer questions like:

- Did this repository, endpoint, or document satisfy the requirement?
- Does submitted work meet written acceptance criteria?
- Is an off-chain event or public data source enough to unlock an action?
- Can another contract safely rely on an already-resolved claim?

This registry gives those applications a common attestation interface.

## Core API

```python
request_attestation(subject, claim, evidence_uri, criteria, ttl_seconds) -> u256
resolve_attestation(request_id) -> None
resolve_github_repo_attestation(request_id) -> None
get_attestation(request_id) -> Attestation
get_latest_by_fingerprint(subject, claim, evidence_uri, criteria) -> u256
is_attested_true(request_id, min_confidence) -> bool
is_attested_false(request_id, min_confidence) -> bool
is_fresh(request_id) -> bool
```

## Result Codes

```text
0 = unknown
1 = true
2 = false
3 = inconclusive
4 = error
```

## Bradbury Proof

The v4 deterministic GitHub resolver was tested on Bradbury.

```text
request_id: 2
subject: github.com/genlayerlabs/genlayer-project-boilerplate
evidence_uri: https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
result: 1
confidence: 9500
reason_code: github_repo_verified
```

Verifier proof:

```text
is_attested_true(2, 7000): true
get_latest_by_fingerprint(...): 2
```

## Repository Layout

```text
contracts/
  outcome_attestation_registry.py

studio_bradbury/
  outcome_attestation_registry.py

examples/
  consumer_contract.py
  genlayer-js-usage.ts

docs/
  index.html
  styles.css
  assets/architecture.svg
  guide.md
  architecture.md
  testing.md
  submission.md

site/
  index.html
  styles.css
  assets/architecture.svg

API_MANIFEST.md
DEPLOYMENT_BRADBURY.md
STUDIO_BRADBURY_TEST_PLAN.md
SUBMISSION_BRIEF.md
TEST_LOG_BRADBURY.md
```

## Start Here

- Open the documentation site locally: [docs/index.html](docs/index.html)
- Read the full guide: [docs/guide.md](docs/guide.md)
- Review the architecture: [docs/architecture.md](docs/architecture.md)
- Reproduce the Bradbury test: [docs/testing.md](docs/testing.md)
- See the submission summary: [docs/submission.md](docs/submission.md)

## Contract Source

The primary contract source is:

[contracts/outcome_attestation_registry.py](contracts/outcome_attestation_registry.py)

The Studio paste-ready copy is:

[studio_bradbury/outcome_attestation_registry.py](studio_bradbury/outcome_attestation_registry.py)
