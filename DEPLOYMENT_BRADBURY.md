# Bradbury Deployment

## Network

GenLayer Bradbury Testnet

## Contract

`OutcomeAttestationRegistry`

## Contract Address

Original v1 deployment:

```text
0xb715ed396892a09381c73e8CE621397577C2c53A
```

Active v4 deployment with successful smoke tests:

```text
0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
```

## Deploy Transaction

```text
0x5258707a90f2b81924a9ae94254718a8a774a9227856b1dc35956bba68abfaee
```

## Deployment Result

```text
statusName: ACCEPTED
resultName: AGREE
txExecutionResultName: FINISHED_WITH_RETURN
```

## Recorded At

```text
2026-08-07T11:06:18Z
```

## Next Test

The first `request_attestation` call succeeded, but the generic `resolve_attestation` calls failed with `UNDETERMINED / DISAGREE / FINISHED_WITH_ERROR`.

Attempting to upgrade in Studio on Bradbury returned:

```text
method not found: gen_getContractNonce
```

Deploy a fresh v3 instance with the current `studio_bradbury/outcome_attestation_registry.py`, then create a new request and run `resolve_github_repo_attestation(new_request_id)`.

## Successful Smoke Test

The active v4 deterministic GitHub resolver passed with:

```text
request_id: 2
result: 1
confidence: 9500
reason_code: github_repo_verified
subject: github.com/genlayerlabs/genlayer-project-boilerplate
evidence_uri: https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate
```

Consumer verifier result:

```text
is_attested_true(2, 7000): true
```

Fingerprint reuse result:

```text
get_latest_by_fingerprint(...): 2
```
