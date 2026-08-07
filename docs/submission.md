# Submission Summary

## Name

`OutcomeAttestationRegistry`

## Category

Reusable GenLayer Intelligent Contract primitive.

## Summary

`OutcomeAttestationRegistry` standardizes consensus-backed attestations for external claims. It lets builders request a claim evaluation, resolve it through a GenLayer resolver profile, store the result, and expose small verifier methods that other contracts and frontends can consume.

## Why It Is Not A Lightweight Contract

This contract is not a one-off app or a learning exercise. It is infrastructure for other GenLayer projects.

It can be used by:

- bounty platforms
- escrow systems
- agent marketplaces
- DAO tooling
- reputation registries
- prediction markets
- policy gates

## What Makes It GenLayer-native

The contract depends on GenLayer's ability to evaluate web evidence and non-deterministic inputs. Normal smart contracts cannot fetch and evaluate external evidence directly, and centralized services would become trusted adjudicators.

GenLayer makes the adjudication itself part of the contract flow.

## Active Bradbury Proof

```text
contract: 0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
request_id: 2
result: 1
confidence: 9500
reason_code: github_repo_verified
is_attested_true(2, 7000): true
get_latest_by_fingerprint(...): 2
```

## Core Reusable Interface

```python
is_attested_true(request_id, min_confidence)
is_attested_false(request_id, min_confidence)
is_fresh(request_id)
```

These methods are the integration surface for downstream builders.
