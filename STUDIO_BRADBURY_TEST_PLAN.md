# Studio Bradbury Test Plan

Use this when deploying `OutcomeAttestationRegistry` in GenLayer Studio on Bradbury Testnet.

Current accepted deployment:

```text
0xb715ed396892a09381c73e8CE621397577C2c53A
```

## Current Patch Level

After the first `resolve_attestation` smoke test, v1 returned `UNDETERMINED / DISAGREE / FINISHED_WITH_ERROR`.

Do not use **Upgrade code** for v3 on Bradbury. Studio returned:

```text
method not found: gen_getContractNonce
```

Also, v3 adds a storage field and a new resolver method, so a fresh deployment is safer than upgrading the old instance.

Use **Deploy new instance** in Studio with the current file:

```text
studio_bradbury/outcome_attestation_registry.py
```

Then rerun `request_attestation` on the new deployment.

Current v3 adds a deterministic resolver profile:

```text
resolve_github_repo_attestation
```

Use this method for the GitHub smoke test instead of the generic LLM resolver.

## Pre-deploy Checks

1. Open GenLayer Studio.
2. Confirm the selected network is `Genlayer Bradbury Testnet`.
3. Confirm the connected wallet has enough GEN for deployment and writes.
4. Create a new contract file named `outcome_attestation_registry.py`.
5. Paste the full contract from `studio_bradbury/outcome_attestation_registry.py`.

The registry does not require constructor arguments.

## Deploy

1. Deploy `outcome_attestation_registry.py`.
2. Save the deployed contract address.
3. Open the deployed contract panel.
4. Confirm these methods appear:

```text
request_attestation
resolve_attestation
resolve_github_repo_attestation
get_attestation
get_latest_by_fingerprint
is_attested_true
is_attested_false
is_fresh
```

## Smoke Test 1: Create A Request

Call `request_attestation` with:

```text
subject:
github.com/genlayerlabs/genlayer-project-boilerplate

claim:
The repository exists and is a GenLayer-related project.

evidence_uri:
https://api.github.com/repos/genlayerlabs/genlayer-project-boilerplate

criteria:
Return true only if the evidence clearly identifies an existing GitHub repository under genlayerlabs and the repository metadata or description indicates it is related to GenLayer. Return inconclusive if the repository cannot be fetched or the relationship is unclear.

ttl_seconds:
604800
```

Expected:

- Transaction finalizes successfully.
- Return value is a `request_id`, usually `1` for the first request.

## Smoke Test 2: Resolve The GitHub Request

Call `resolve_github_repo_attestation` with:

```text
request_id:
1
```

Expected:

- Transaction finalizes successfully.
- The resolver stores a structured attestation.
- For the provided GitHub payload, the result should be `true` with high confidence if GitHub returns `200`.
- If GitHub cannot be fetched, v3 should store a structured `error` or `inconclusive` attestation instead of failing execution.
- v4 does not read `status_code` from `gl.nondet.web.get()` because Bradbury's `get()` response exposes `body` but not `status_code`.
- The original `genlayer-simulator` payload can return inconclusive if GitHub does not provide stable repository identity fields. Use `genlayer-project-boilerplate` for the positive smoke test.

## Smoke Test 3: Read The Attestation

Call `get_attestation` with:

```text
request_id:
1
```

Expected:

- `result` is one of `1`, `2`, `3`, or `4`.
- `confidence` is between `0` and `10000`.
- `summary` is non-empty.
- `evidence_digest` is non-empty.
- `expires_at` is greater than `created_at`.

## Smoke Test 4: Consumer API

Call `is_fresh`:

```text
request_id:
1
```

Expected:

```text
true
```

Call `is_attested_true`:

```text
request_id:
1
min_confidence:
7000
```

Expected:

- `true` if the attestation result is true and confidence is at least `7000`.
- `false` otherwise.

## Smoke Test 5: Fingerprint Reuse

Call `request_attestation` again with the exact same inputs from Smoke Test 1.

Expected:

- It returns the existing fresh `request_id` instead of creating a duplicate.

## Edge Test: Invalid Request

Call `get_attestation` with:

```text
request_id:
999999
```

Expected:

- User error: `unknown attestation`.

## Notes

- The contract avoids token transfers and contract-to-contract writes, which keeps it compatible with the current Studio limitations shown in the Studio home screen.
- The resolver depends on web and LLM nondeterminism, so the final result can be `inconclusive` if evidence is missing, unstable, or insufficient.
- For a stronger public demo, use evidence URLs with stable JSON responses rather than frequently changing pages.
