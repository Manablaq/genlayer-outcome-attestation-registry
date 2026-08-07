import { createAccount, createClient } from "genlayer-js";
import { testnetAsimov } from "genlayer-js/chains";
import { ExecutionResult, TransactionStatus } from "genlayer-js/types";

const account = createAccount();
const client = createClient({
  chain: testnetAsimov,
  account,
});

const registryAddress = "0x...";

const requestTx = await client.writeContract({
  address: registryAddress,
  functionName: "request_attestation",
  args: [
    "github.com/genlayerlabs/example-project",
    "The latest main branch CI run is passing.",
    "https://api.github.com/repos/genlayerlabs/example-project/actions/runs?branch=main&per_page=1",
    "Return true only if the latest workflow run conclusion is success. Return inconclusive if no latest completed run is present.",
    BigInt(7 * 24 * 60 * 60),
  ],
  value: BigInt(0),
});

const requestReceipt = await client.waitForTransactionReceipt({
  hash: requestTx,
  status: TransactionStatus.FINALIZED,
});

if (requestReceipt.txExecutionResultName !== ExecutionResult.FINISHED_WITH_RETURN) {
  throw new Error("request_attestation failed");
}

// In a production app, decode/read the returned request id according to the
// current SDK receipt shape, or fetch it by fingerprint.
const requestId = await client.readContract({
  address: registryAddress,
  functionName: "get_latest_by_fingerprint",
  args: [
    "github.com/genlayerlabs/example-project",
    "The latest main branch CI run is passing.",
    "https://api.github.com/repos/genlayerlabs/example-project/actions/runs?branch=main&per_page=1",
    "Return true only if the latest workflow run conclusion is success. Return inconclusive if no latest completed run is present.",
  ],
  stateStatus: "accepted",
});

const resolveTx = await client.writeContract({
  address: registryAddress,
  functionName: "resolve_attestation",
  args: [requestId],
  value: BigInt(0),
});

const resolveReceipt = await client.waitForTransactionReceipt({
  hash: resolveTx,
  status: TransactionStatus.FINALIZED,
});

if (resolveReceipt.txExecutionResultName !== ExecutionResult.FINISHED_WITH_RETURN) {
  throw new Error("resolve_attestation failed");
}

const verified = await client.readContract({
  address: registryAddress,
  functionName: "is_attested_true",
  args: [requestId, 8000],
  stateStatus: "accepted",
});

console.log({ requestId, verified });
