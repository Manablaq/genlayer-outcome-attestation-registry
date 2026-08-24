import { createHash } from "node:crypto";
import { createAccount, createClient } from "genlayer-js";
import { testnetAsimov } from "genlayer-js/chains";
import { ExecutionResult, TransactionStatus } from "genlayer-js/types";

const account = createAccount();
const client = createClient({ chain: testnetAsimov, account });
const registryAddress = "0x...";

const primaryUri = "https://www.iana.org/help/example-domains";
const response = await fetch(primaryUri);
if (!response.ok) throw new Error(`evidence fetch failed: ${response.status}`);
const primaryBytes = Buffer.from(await response.arrayBuffer());
const primarySha256 = createHash("sha256").update(primaryBytes).digest("hex");

const observedAt = BigInt(Math.floor(Date.now() / 1000));
const maxEvidenceAge = BigInt(24 * 60 * 60);
const attestationTtl = BigInt(60 * 60);
const args = [
  "IANA Example Domains",
  "example.com and example.org are maintained for documentation purposes.",
  primaryUri,
  primarySha256,
  "Internet Assigned Numbers Authority",
  "",
  "",
  "",
  "IANA Example Domains page observed 2026-08-24",
  "Return true only if the hash-pinned evidence explicitly supports the claim; otherwise return inconclusive.",
  observedAt,
  maxEvidenceAge,
  1,
  attestationTtl,
] as const;

const expectedFingerprint = await client.readContract({
  address: registryAddress,
  functionName: "compute_fingerprint",
  args,
  stateStatus: "accepted",
});

const requestTx = await client.writeContract({
  address: registryAddress,
  functionName: "request_attestation",
  args,
  value: BigInt(0),
});
const requestReceipt = await client.waitForTransactionReceipt({
  hash: requestTx,
  status: TransactionStatus.FINALIZED,
});
if (requestReceipt.txExecutionResultName !== ExecutionResult.FINISHED_WITH_RETURN) {
  throw new Error("request_attestation failed");
}

const requestId = await client.readContract({
  address: registryAddress,
  functionName: "get_latest_by_fingerprint",
  args: [expectedFingerprint],
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
  functionName: "is_attested_true_for",
  args: [requestId, expectedFingerprint, BigInt(30 * 60)],
  stateStatus: "accepted",
});

console.log({ requestId, expectedFingerprint, primarySha256, verified });
