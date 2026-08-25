# Bradbury Test Log

## Hardened v2.1 Release

```text
contract: PENDING_FRESH_DEPLOYMENT
deployment_tx: PENDING_FRESH_DEPLOYMENT
source_commit: 60eed18e3861d650bad9895e5b43b277404159a9
source_sha256: 901a941a30da36af7b278094435d45f834e98d17042b3abfe7321add3fc5369c
local_tests: 14 passing
genvm_linter: PASS (lint + SDK validation)
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

## Superseded v2 Candidate Regression

Candidate contract: `0x981C81A7b532Ca062a1443EB43cd294d8E6d6558`.
These transactions demonstrate the core security boundary, but the candidate is
not the final release because the missing-record read exposed an uncontrolled
`AttributeError` that v2.1 fixes.

| Regression | Evidence | Observed result |
| --- | --- | --- |
| Deploy v2 candidate | [transaction](https://explorer-bradbury.genlayer.com/tx/0xcaa934bf722f484b6edaaf0629f7f39f7c8a4d9a5deb91fc23df061ee81e0505) | accepted; unanimous `AGREE`; return |
| Register two-source request | [transaction](https://explorer-bradbury.genlayer.com/tx/0x98f85114f8787e69854b4c876ab69955173edc4468bbb9b6a7559dc50eb8e53f) | fingerprint `01f31f...a3890`; request `1` |
| Resolve matching evidence | [transaction](https://explorer-bradbury.genlayer.com/tx/0xeac8f145252a19470a7417ce6b901009c9ad9dc8a3d0790f8ff2f2af4dbe5973) | true; both hashes matched; verified sources `2` |
| Bound consumer reads | CLI views | exact fingerprint `true`; substituted fingerprint `false` |
| Register incorrect hash | [transaction](https://explorer-bradbury.genlayer.com/tx/0xdab7ffacaadcf6e03c229e2d53ffdfbec4ce39337bfed2b13758913b99d2fe11) | request `2` accepted |
| Reject incorrect hash | [transaction](https://explorer-bradbury.genlayer.com/tx/0xceda4a932294beff8fef05fb3aafc1d92d4c16ae0c7c7744cd676c93ca1b84ed) | `integrity_ok: false`; execution error |
| Reject stale observation | [transaction](https://explorer-bradbury.genlayer.com/tx/0x92eab86eb2f0a7229e6db6acd7b868bd7e47998a50b1e6d70669493410123070) | unanimous rejection; execution error |

## Historical Evidence

Contract `0x78C17d55FB0eA3d768527793749e1AC878b0572C` and deployment
transaction `0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882`
are historical only. Their true and false smoke tests do not prove the hardened
evidence commitment and consumer-binding rules.
