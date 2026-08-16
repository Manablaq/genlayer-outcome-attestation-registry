# Submission Brief

## Outcome Attestation Registry

A reusable GenLayer Intelligent Contract primitive for turning public evidence into strict-consensus, integration-ready attestations.

## What Makes It Safe to Compose

Every validator independently fetches the registered evidence and reapplies the request's immutable criteria. Strict equality binds the complete canonical result, including result, derived confidence, reason, summary, and evidence digest. The registry writes only after agreement, then marks the record `consensus_bound`. Consumer methods accept only fresh records with that binding and the exact requested outcome.

## Why It Is Reusable

Escrows, bounties, prediction markets, DAOs, agent workflows, and reputation systems can request and reuse a common evidence-backed answer rather than embedding a trusted resolver. Canonical fingerprints prevent duplicate fresh work and expiry lets consumers reject stale results.

## Corrected Deployment Evidence

Use the fresh Bradbury address, accepted deployment transaction, and post-deployment independent-consensus smoke test recorded after deploying the corrected matching Studio source. The previous deployment is historical only.
