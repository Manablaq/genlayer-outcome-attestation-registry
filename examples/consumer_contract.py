# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *


@gl.contract_interface
class OutcomeAttestationRegistry:
    class View:
        def is_attested_true(self, request_id: u256, min_confidence: u32) -> bool: ...
        def is_fresh(self, request_id: u256) -> bool: ...

    class Write:
        pass


class AttestationGatedAction(gl.Contract):
    registry: Address
    executed: TreeMap[u256, bool]

    def __init__(self, registry: Address):
        self.registry = registry

    @gl.public.write
    def execute_if_verified(self, request_id: u256) -> None:
        if self.executed.get(request_id, False):
            raise gl.vm.UserError("already executed")

        registry = OutcomeAttestationRegistry(self.registry)
        if not registry.view().is_fresh(request_id):
            raise gl.vm.UserError("attestation expired")
        if not registry.view().is_attested_true(request_id, u32(8000)):
            raise gl.vm.UserError("attestation not verified")

        self.executed[request_id] = True
        # Put application-specific action here: release escrow, mint badge,
        # mark bounty complete, update reputation, or resolve a market.
