# Bradbury Deployment Record

## Hardened Release — Deployment Required

```text
contract: PENDING_FRESH_DEPLOYMENT
deployment_tx: PENDING_FRESH_DEPLOYMENT
deployment_status: PENDING
source_commit: PENDING_FINAL_COMMIT
source_sha256: PENDING_FINAL_COMMIT
```

The hardened source adds collision-resistant specification fingerprints,
full-response SHA-256 commitments, authority/version metadata, explicit
freshness and corroboration policies, and fingerprint-bound consumer methods.
It requires a new contract address because the public storage schema and API
changed.

Do not mark this release submission-ready until the deployment and every live
regression in `STUDIO_BRADBURY_TEST_PLAN.md` are recorded.

## Historical Deployments — Not Valid for This Release

```text
contract: 0x78C17d55FB0eA3d768527793749e1AC878b0572C
deployment_tx: 0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882
source_commit: 193a7192d22135c2b1e85fe5d71d2644a56705c9
```

That contract proved the corrected nondeterministic boundary but retained
collision-prone request identity, mutable evidence identification, and
request-ID-only consumer views. Earlier contract
`0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63` is also historical.
