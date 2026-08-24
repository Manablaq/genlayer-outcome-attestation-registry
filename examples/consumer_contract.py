# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *


@gl.contract_interface
class OutcomeAttestationRegistry:
    class View:
        def is_attested_true_for(
            self,
            request_id: u256,
            expected_fingerprint: str,
            consumer_max_age_seconds: u256,
        ) -> bool: ...

    class Write:
        pass


class AttestationGatedAction(gl.Contract):
    registry: Address
    expected_fingerprint: str
    consumer_max_age_seconds: u256
    executed: TreeMap[u256, bool]

    def __init__(
        self,
        registry: Address,
        expected_fingerprint: str,
        consumer_max_age_seconds: u256,
    ):
        self.registry = registry
        self.expected_fingerprint = expected_fingerprint
        self.consumer_max_age_seconds = consumer_max_age_seconds

    @gl.public.write
    def execute_if_verified(self, request_id: u256) -> None:
        if self.executed.get(request_id, False):
            raise gl.vm.UserError("already executed")

        registry = OutcomeAttestationRegistry(self.registry)
        if not registry.view().is_attested_true_for(
            request_id,
            self.expected_fingerprint,
            self.consumer_max_age_seconds,
        ):
            raise gl.vm.UserError("attestation is not bound, fresh, and true")

        self.executed[request_id] = True
        # Put application-specific action here: release escrow, mint badge,
        # mark bounty complete, update reputation, or resolve a market.
