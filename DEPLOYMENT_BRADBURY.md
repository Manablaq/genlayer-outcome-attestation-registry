# Bradbury Deployment Record

## Historical Deployment - Not Valid for Resubmission

```text
contract: 0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
deployment_tx: 0x5258707a90f2b81924a9ae94254718a8a774a9227856b1dc35956bba68abfaee
```

This deployment predates the one-boundary independent-validation redesign and must not be cited as the corrected contract.

## Corrected Deployment

```text
contract: 0x78C17d55FB0eA3d768527793749e1AC878b0572C
deployment_tx: 0x1227e1fe770f43c693f599c310be1eedaabdc0d24ef5eeb2aba811f4b08f5882
deployment_status: ACCEPTED
source_commit: 193a7192d22135c2b1e85fe5d71d2644a56705c9
source_match: contracts/outcome_attestation_registry.py == studio_bradbury/outcome_attestation_registry.py
```

The deployment source removes the prior GitHub-specific resolver. It uses one global non-deterministic evaluator with no storage writes in the callback. Each validator independently fetches the registered evidence and reapplies immutable criteria; strict equality binds the result, derived confidence, reason code, summary, and evidence digest before state is written.

Post-deployment evidence is recorded in [TEST_LOG_BRADBURY.md](TEST_LOG_BRADBURY.md). Both the true and false paths completed with `consensus_bound: true` and mutually exclusive consumer checks.
