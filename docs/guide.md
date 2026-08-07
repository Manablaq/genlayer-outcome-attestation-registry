# Outcome Attestation Registry Guide

## Overview

`OutcomeAttestationRegistry` is a reusable GenLayer Intelligent Contract that turns external evidence into structured, reusable attestations.

An attestation is a stored judgment about a claim:

```text
subject + claim + evidence_uri + criteria -> result + confidence + reason
```

The contract is designed as infrastructure. Other GenLayer builders can use it as a registry for verified claims instead of duplicating web access, AI prompts, storage schemas, expiry handling, and verifier methods in every contract.

## Main Concepts

### Subject

The thing the claim is about.

Examples:

```text
github.com/genlayerlabs/genlayer-project-boilerplate
invoice:INV-2039
dao-proposal:42
agent-task:0xabc...
```

### Claim

The statement being evaluated.

Example:

```text
The repository exists and is a GenLayer-related project.
```

### Evidence URI

The web resource used as evidence.

Example:

```text
https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
```

### Criteria

The rule the resolver must apply.

Example:

```text
Return true only if the evidence clearly identifies an existing GitHub repository under genlayerlabs and the repository metadata or description indicates it is related to GenLayer.
```

### Fingerprint

The contract canonicalizes the subject, claim, evidence URI, and criteria into a fingerprint. Fresh duplicate requests reuse the existing attestation instead of forcing another resolution.

## Resolver Profiles

The contract supports a generic resolver and a deterministic resolver profile.

### Generic Resolver

```python
resolve_attestation(request_id)
```

This path is intended for semantic or document-style claims that need AI judgment. It uses web evidence and an LLM inside GenLayer nondeterministic execution, then stores a normalized result.

### GitHub Repository Resolver

```python
resolve_github_repo_attestation(request_id)
```

This path is intended for GitHub repository existence and metadata claims. It fetches a GitHub API response, normalizes stable fields, uses strict equality over the normalized snapshot, and applies deterministic logic after consensus.

This profile was added because structured API evidence should not depend on an LLM when deterministic checks are enough.

## Typical Flow

1. Call `request_attestation`.
2. Save the returned request id.
3. Call the correct resolver profile.
4. Call `get_attestation` to inspect the result.
5. Use `is_attested_true`, `is_attested_false`, or `is_fresh` in downstream integrations.

## Example

Request:

```text
subject: github.com/genlayerlabs/genlayer-project-boilerplate
claim: The repository exists and is a GenLayer-related project.
evidence_uri: https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
ttl_seconds: 604800
```

Resolve:

```text
resolve_github_repo_attestation(2)
```

Read:

```text
get_attestation(2)
```

Expected positive result:

```text
result: 1
confidence: 9500
reason_code: github_repo_verified
```

## Integration Pattern

Downstream contracts do not need to parse the full attestation.

They can call:

```python
is_attested_true(request_id, min_confidence)
```

Example use cases:

- release escrow after verified task completion
- mark a bounty as complete
- resolve a prediction market outcome
- mint a reputation credential
- gate a DAO action behind verified evidence
- check whether an agent completed a job

## Design Guarantees

- Attestations are structured, not prose-only.
- Confidence is stored as an integer from `0` to `10000`.
- Results use stable numeric codes.
- Fresh duplicate requests are reusable by fingerprint.
- Expired attestations are rejected by verifier methods.
- Resolver profiles can be added without changing the core registry interface.

## Important Notes

This project remains an Intelligent Contract project. The site and docs explain the contract; they are not the product. The core artifact is still:

```text
contracts/outcome_attestation_registry.py
```
