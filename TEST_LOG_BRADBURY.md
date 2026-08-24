# Bradbury Test Log

## Hardened Release

```text
contract: PENDING_FRESH_DEPLOYMENT
deployment_tx: PENDING_FRESH_DEPLOYMENT
source_commit: PENDING_FINAL_COMMIT
source_sha256: PENDING_FINAL_COMMIT
local_tests: 13 passing
```

## Required Live Evidence

| Regression | Transaction / read | Expected result |
| --- | --- | --- |
| Deploy exact committed source | Pending | `AGREE`, return |
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
