# Studio Bradbury Test Plan

## Deploy

1. Create `outcome_attestation_registry.py` in GenLayer Studio.
2. Paste `studio_bradbury/outcome_attestation_registry.py` exactly.
3. Confirm it matches `contracts/outcome_attestation_registry.py` byte-for-byte.
4. Deploy a new instance, save the address, and record the accepted deployment transaction.

## Smoke Test 1: Request

Call `request_attestation` with a stable public HTTPS evidence URL and explicit, binary criteria.

```text
Return true only if the registered evidence explicitly supports the claim. Return false only if it explicitly supports the opposite. Otherwise return inconclusive.
```

## Smoke Test 2: Resolve

Call `resolve_attestation(request_id)`.

Expected behavior:

- Every validator fetches the registered URI and reapplies the same request criteria.
- `strict_eq` compares result, derived confidence, reason code, summary, and evidence digest.
- The only storage write occurs after that agreement.

## Smoke Test 3: Bind Consumer Views

Call `get_attestation(request_id)`. Confirm `consensus_bound: true`, then call `is_attested_true(request_id, 9500)` and `is_attested_false(request_id, 9500)`.

Only the verifier that matches the stored canonical result may return `true`.

## Regression Requirement

Do not use `resolve_github_repo_attestation`; it was removed. The corrected contract has one evidence resolver path and no nested nondeterminism or resolver storage writes.
