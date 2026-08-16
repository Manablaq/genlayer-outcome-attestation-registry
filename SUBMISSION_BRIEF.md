# Submission Brief

## Outcome Attestation Registry

A reusable GenLayer Intelligent Contract primitive for turning public evidence into strict-consensus, integration-ready attestations.

## What Makes It Safe to Compose

Every validator independently fetches the registered evidence and reapplies the request's immutable criteria. Strict equality binds the complete canonical result, including result, derived confidence, reason, summary, and evidence digest. The registry writes only after agreement, then marks the record `consensus_bound`. Consumer methods accept only fresh records with that binding and the exact requested outcome.

## Why It Is Reusable

Escrows, bounties, prediction markets, DAOs, agent workflows, and reputation systems can request and reuse a common evidence-backed answer rather than embedding a trusted resolver. Canonical fingerprints prevent duplicate fresh work and expiry lets consumers reject stale results.

## Corrected Deployment Evidence

```text
corrected_contract: 0x78C17d55FB0eA3d768527793749e1AC878b0572C
accepted_deployment_tx: 0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882
corrected_source_commit: 193a7192d22135c2b1e85fe5d71d2644a56705c9
```

The corrected deployment was exercised through both outcomes:

```text
true path:  request 1, resolve 0xb4ac684d8f6edb5cd97de6e9c2a9fdd8bec671164ff83d9e05933b9022ec1162
            is_attested_true(1, 9500) = true
            is_attested_false(1, 9500) = false

false path: request 2, resolve 0xb55ba8d0ced3aad33ff4e2a253c952711abcc9f20981bb473e3b507695e45485
            is_attested_false(2, 9500) = true
            is_attested_true(2, 9500) = false
```

The previous deployment is historical only. See `DEPLOYMENT_BRADBURY.md` and `TEST_LOG_BRADBURY.md` for the full evidence trail.
