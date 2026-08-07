# Submission Brief

## Contract

`OutcomeAttestationRegistry`

Repository:

```text
https://github.com/Manablaq/genlayer-outcome-attestation-registry
```

Active Bradbury deployment:

```text
0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
```

## Category

Reusable Intelligent Contract primitive.

## One-line Summary

A composable registry for requesting, resolving, caching, and consuming GenLayer consensus-backed attestations about real-world, web, document, or AI-evaluated claims.

## Problem

Many GenLayer applications need to answer questions that deterministic contracts cannot answer:

- Did an external event happen?
- Does a web endpoint prove a condition?
- Does submitted work satisfy natural-language criteria?
- Is a document, policy, or agent output compliant with a rule?

Without a shared primitive, each builder has to rebuild the same request lifecycle, nondeterministic web/LLM calls, prompt-injection defenses, validator logic, result normalization, expiry handling, and consumer-facing view methods.

## Primitive Provided

The registry standardizes a reusable attestation object:

```text
subject + claim + evidence_uri + criteria -> result + confidence + reason + expiry
```

Other contracts can consume the result through simple methods like:

```python
is_attested_true(request_id, min_confidence)
is_attested_false(request_id, min_confidence)
is_fresh(request_id)
```

## Why This Is Reusable

This contract can be integrated by:

- escrow contracts releasing funds on verified task completion
- bounty platforms checking whether work meets requirements
- prediction markets resolving outcomes
- DAO tooling verifying proposal summaries or off-chain votes
- agent marketplaces judging whether an agent completed a job
- reputation systems recording evidence-backed claims
- policy gates checking whether submitted content follows written rules

## Why GenLayer Is Needed

The core resolution step depends on web data, unstructured evidence, and natural-language criteria. A normal smart contract cannot evaluate those inputs by itself, while a centralized backend would become the trusted adjudicator. GenLayer validators can independently evaluate the evidence and reach a shared result through consensus.

## Key Design Choices

- Structured outputs instead of vague prose.
- Result codes instead of app-specific strings.
- Confidence in basis points for deterministic comparison.
- Canonical fingerprints to reuse fresh duplicate attestations.
- Expiration so consumers can reject stale claims.
- Evidence treated as untrusted prompt content.
- Nondeterministic work isolated inside resolver functions.
- Storage writes happen only after consensus returns.

## Acceptance-bar Fit

This is not a learning exercise or a small variation of an existing app contract. It is a general-purpose adjudication layer that other GenLayer builders can compose into many different products.

## Bradbury Smoke Test

The v4 contract was tested on GenLayer Bradbury Testnet with the deterministic GitHub resolver:

```text
subject: github.com/genlayerlabs/genlayer-project-boilerplate
evidence_uri: https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
result: true
confidence: 9500
reason_code: github_repo_verified
```
