# Submission Summary

`OutcomeAttestationRegistry` provides a reusable evidence-attestation primitive for GenLayer builders.

Its security boundary is explicit: validators independently fetch evidence and reapply immutable criteria; strict equality binds every consequential output; only the agreed canonical result is written; consumer views require that consensus binding. This prevents a leader response whose JSON merely looks valid from authorizing a contradictory downstream outcome.

The corrected deployment evidence must use the fresh address and accepted transaction recorded after redeployment. The previous v4 address is not the corrected deployment.
