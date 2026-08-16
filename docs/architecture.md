# Architecture

```text
request snapshot -> independent evidence fetch and criteria evaluation
                 -> strict equality of canonical result
                 -> bound attestation storage -> consumer verifier
```

`_evaluate_attestation_snapshot` is the only non-deterministic boundary. It reads an immutable snapshot, fetches its evidence, and derives canonical JSON. It has no storage writes, transfers, or nested consensus calls.

`resolve_attestation` runs that evaluator through `gl.eq_principle.strict_eq`, validates the agreed payload, then writes the `Attestation` with `consensus_bound = true`. `is_attested_true` and `is_attested_false` bind consequential downstream reads to this state.

The previous GitHub-special resolver was removed, so generic evidence resolution is the sole auditable path.
