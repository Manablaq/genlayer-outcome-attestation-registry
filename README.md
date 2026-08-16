# Outcome Attestation Registry

`OutcomeAttestationRegistry` is a reusable GenLayer Intelligent Contract primitive for creating, resolving, caching, and consuming consensus-bound attestations about public evidence.

```text
subject + claim + evidence URI + criteria -> independently verified attestation
```

## Security Model

`resolve_attestation` has one pure non-deterministic boundary. Each validator independently fetches the request's registered evidence, applies the immutable request criteria, and derives the complete canonical result. `gl.eq_principle.strict_eq` requires the entire canonical payload to agree before storage is written.

The stored attestation records the result, canonical confidence, reason code, summary, evidence digest, and `consensus_bound = true`. `is_attested_true` and `is_attested_false` require that binding, freshness, the exact stored result, and the requested confidence threshold. A schema-valid leader response cannot by itself change a downstream outcome.

## Core API

```python
request_attestation(subject, claim, evidence_uri, criteria, ttl_seconds) -> u256
resolve_attestation(request_id) -> None
get_attestation(request_id) -> Attestation
get_latest_by_fingerprint(subject, claim, evidence_uri, criteria) -> u256
is_attested_true(request_id, min_confidence) -> bool
is_attested_false(request_id, min_confidence) -> bool
is_fresh(request_id) -> bool
```

There is no GitHub-specific resolver. GitHub URLs use the same generic evidence path, eliminating the prior nested non-deterministic and storage-writing resolver shape.

## Canonical Results

```text
true          confidence 9500
false         confidence 9500
inconclusive  confidence 6000
error         confidence 0
```

Confidence is derived from the agreed result rather than model-controlled metadata.

## Deployment Status

The prior deployment at `0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63` is historical and must not be presented as the corrected contract.

```text
Corrected Bradbury contract: 0x78C17d55FB0eA3d768527793749e1AC878b0572C
Accepted deployment tx:     0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882
Corrected source commit:    193a7192d22135c2b1e85fe5d71d2644a56705c9
```

The corrected contract completed both true and false consensus-bound smoke tests at confidence `9500`; see [TEST_LOG_BRADBURY.md](TEST_LOG_BRADBURY.md).

## Repository Layout

```text
contracts/outcome_attestation_registry.py        Primary source
studio_bradbury/outcome_attestation_registry.py  Byte-identical Studio source
tests/test_consensus_design.py                    Regression checks for consensus design
docs/                                             Guide, architecture, test, and submission material
```

The registry is composable by escrow systems, bounties, prediction markets, DAOs, agent workflows, policy gates, and reputation systems.
