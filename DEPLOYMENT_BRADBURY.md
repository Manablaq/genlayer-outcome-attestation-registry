# Bradbury Deployment Record

## Historical Deployment - Not Valid for Resubmission

```text
contract: 0xd660ef089b4798e9c47B94CDDDE0EcEe5Fd29F63
deployment_tx: 0x5258707a90f2b81924a9ae94254718a8a774a9227856b1dc35956bba68abfaee
```

This deployment predates the one-boundary independent-validation redesign and must not be cited as the corrected contract.

## Corrected Deployment Checklist

After deploying `studio_bradbury/outcome_attestation_registry.py`, record:

```text
contract: <new Bradbury address>
deployment_tx: <accepted deployment transaction>
source_commit: <commit containing this redesign>
source_match: contracts/outcome_attestation_registry.py == studio_bradbury/outcome_attestation_registry.py
```

Submit only after an accepted `resolve_attestation` transaction proves `consensus_bound: true` and a matching consumer verifier call succeeds.
