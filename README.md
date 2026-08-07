# Outcome Attestation Registry

`OutcomeAttestationRegistry` is a reusable GenLayer Intelligent Contract primitive for creating, resolving, caching, and consuming consensus-backed attestations about claims.

It is designed for other builders to integrate into escrow contracts, prediction markets, bounty platforms, DAO tooling, reputation systems, agent marketplaces, and policy gates.

Repository:

```text
https://github.com/Manablaq/genlayer-outcome-attestation-registry
```

Active Bradbury deployment:

```text
0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
```

## Why This Matters

Many GenLayer applications need the same hard thing: evaluate a real-world or AI-readable claim using web data, documents, or natural-language criteria. Without a shared primitive, every app has to reimplement request tracking, prompt safety, consensus validation, result normalization, expiry, and consumer APIs.

This registry gives builders a standard interface:

1. Request an attestation.
2. Resolve it through GenLayer's AI/web consensus.
3. Let any contract read the result through small view methods.

## What It Stores

Each attestation stores:

- requester
- subject
- claim
- evidence URI
- acceptance criteria
- canonical fingerprint
- result code
- confidence in basis points from `0` to `10000`
- reason code
- short summary
- evidence digest
- creation, resolution, and expiry timestamps
- resolver address

Result codes:

```text
0 = unknown
1 = true
2 = false
3 = inconclusive
4 = error
```

## Public API

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

## Design Notes

- Duplicate requests reuse fresh attestations via canonical fingerprints.
- Resolver profiles are supported. Structured API claims can use deterministic profile resolvers; semantic claims can use the generic LLM resolver.
- Nondeterministic web and LLM work happens only inside the resolver's nondet block.
- Storage writes happen only after consensus returns an agreed structured result.
- Evidence is treated as untrusted text inside prompts to reduce prompt injection risk.
- The validator accepts only schema-valid outputs with matching verdicts, matching evidence digest, and bounded confidence drift.
- Consumer contracts do not need to parse prose; they can call `is_attested_true` or `is_attested_false`.

## Example Claim

```text
Subject: github.com/genlayerlabs/example-project
Claim: The latest main branch CI run is passing.
Evidence URI: https://api.github.com/repos/genlayerlabs/example-project/actions/runs?branch=main&per_page=1
Criteria: Return true only if the latest workflow run conclusion is success. Return inconclusive if the response does not clearly contain a latest completed run.
```

## Files

- `contracts/outcome_attestation_registry.py` - the Intelligent Contract.
- `studio_bradbury/outcome_attestation_registry.py` - frozen paste-ready Studio/Bradbury deployment copy.
- `examples/consumer_contract.py` - a minimal contract that consumes attestations.
- `examples/genlayer-js-usage.ts` - frontend/SDK usage sketch.
- `API_MANIFEST.md` - exact public API and storage schema.
- `DEPLOYMENT_BRADBURY.md` - accepted Bradbury deployment record.
- `STUDIO_BRADBURY_TEST_PLAN.md` - manual deploy and smoke-test checklist.

## Submission Positioning

This is a primitive, not a one-off app. It standardizes reusable outcome adjudication for the GenLayer ecosystem.
