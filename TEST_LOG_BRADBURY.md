# Bradbury Test Log

## Hardened Release

```text
contract: 0x981C81A7b532Ca062a1443EB43cd294d8E6d6558
deployment_tx: 0xcaa934bf722f484b6edaaf0629f7f39f7c8a4d9a5deb91fc23df061ee81e0505
source_commit: 0868930e7040d3b7205f9d80ec5b021d34df2ee5
source_sha256: ed1be6469644d4ae194988ee0877673e9ad11e8e4daeca5a85f849d943c8d920
local_tests: 14 passing
```

## Required Live Evidence

| Regression | Transaction / read | Expected result |
| --- | --- | --- |
| Deploy exact committed source | [Explorer](https://explorer-bradbury.genlayer.com/tx/0xcaa934bf722f484b6edaaf0629f7f39f7c8a4d9a5deb91fc23df061ee81e0505) | accepted; unanimous `AGREE`; `FINISHED_WITH_RETURN`; finalization pending |
| Create hash-pinned request | Pending | accepted request ID |
| Resolve matching evidence | Pending | `content_verified: true` |
| Read stored full-body hash | Pending | equals registered SHA-256 |
| Consume with exact fingerprint | Pending | matching outcome `true` |
| Consume with substituted fingerprint | Pending | `false` |
| Resolve incorrect evidence hash | Pending | execution error, no attestation |
| Resolve two-source request | Pending | `verified_source_count: 2` |
| Submit stale observation | Pending | execution error |

## Historical Evidence

Contract `0x78C17d55FB0eA3d768527793749e1AC878b0572C` and deployment
transaction `0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882`
are historical only. Their true and false smoke tests do not prove the hardened
evidence commitment and consumer-binding rules.
