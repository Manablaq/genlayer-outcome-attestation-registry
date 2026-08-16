# Bradbury Test Log

## Historical Result

The tests for `0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63` are historical only. That version included a GitHub-specific resolver structure that is not part of the corrected source.

## Corrected Deployment

```text
contract: 0x78C17d55FB0eA3d768527793749e1AC878b0572C
deployment_tx: 0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882
deployment_status: ACCEPTED
source_commit: 193a7192d22135c2b1e85fe5d71d2644a56705c9
```

## Corrected Live Results

The following tests use the generic independent-evaluation path with the IANA Example Domains page as registered evidence and this immutable criterion:

```text
Return true only if the registered evidence explicitly supports the claim.
Return false only if it explicitly supports the opposite.
Otherwise return inconclusive.
```

### True Path

```text
request_tx: 0x4ffd8fabb013a3e9d084c483867008bd5feff495080be27e9c95b88b03afc289
resolve_tx: 0xb4ac684d8f6edb5cd97de6e9c2a9fdd8bec671164ff83d9e05933b9022ec1162
request_id: 1
result: true
confidence: 9500
consensus_bound: true
is_attested_true(1, 9500): true
is_attested_false(1, 9500): false
is_fresh(1): true
```

### False Path

```text
request_tx: 0xe25b831ee4172f97a26de54393177113e9d919a8dfe3d3266fd9257bf797d55e
resolve_tx: 0xb55ba8d0ced3aad33ff4e2a253c952711abcc9f20981bb473e3b507695e45485
request_id: 2
result: false
confidence: 9500
consensus_bound: true
is_attested_false(2, 9500): true
is_attested_true(2, 9500): false
```

The true and false consumer functions cannot both authorize the same stored result. Confidence is derived from the agreed canonical result and checked by each consumer at the requested threshold.

## Test Procedure

```text
request_attestation
resolve_attestation
get_attestation with consensus_bound: true
is_attested_true or is_attested_false at canonical confidence
```

The corrected resolver performs no storage writes inside non-deterministic evaluation and requires validators to independently verify all consequential outputs before strict equality permits storage.
