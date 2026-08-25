# Bradbury Deployment Record

## Hardened Release — Live Verification In Progress

```text
contract: 0x981C81A7b532Ca062a1443EB43cd294d8E6d6558
deployment_tx: 0xcaa934bf722f484b6edaaf0629f7f39f7c8a4d9a5deb91fc23df061ee81e0505
deployment_status: ACCEPTED (finalization pending)
source_commit: 0868930e7040d3b7205f9d80ec5b021d34df2ee5
source_sha256: ed1be6469644d4ae194988ee0877673e9ad11e8e4daeca5a85f849d943c8d920
```

The hardened source adds collision-resistant specification fingerprints,
full-response SHA-256 commitments, authority/version metadata, explicit
freshness and corroboration policies, and fingerprint-bound consumer methods.
It requires a new contract address because the public storage schema and API
changed.

The exact committed source deployed successfully with an `AGREE` consensus and
`FINISHED_WITH_RETURN`. Do not mark this release submission-ready until the
transaction is finalized and every live regression in
`STUDIO_BRADBURY_TEST_PLAN.md` is recorded.

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
