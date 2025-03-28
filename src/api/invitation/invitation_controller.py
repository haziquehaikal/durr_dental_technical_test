from fastapi import APIRouter, Depends
from src.api.invitation.invitation_service import InvitationService
from src.common.models import CreateInvitation, CheckInvitationStatus
from src.common.middleware import admin_required
# init router
router = APIRouter(
    prefix="/invitation",
    tags=["invitation"]
)

# API routes


class InvitationController:

    @router.post("/create")
    def create_invitation(payload: CreateInvitation, user=Depends(admin_required)):
        return InvitationService.create_invitation(payload)

    @router.get("/checkstatus")
    def get_invitation_status(email: str, code: str):
        return InvitationService.check_invitation_status(email, code)

    @router.patch("/confirm")
    def comfirm_invitation(payload: CheckInvitationStatus):
        return InvitationService.confirm_invitation(payload)

    @router.delete("/delete")
    def delete_invitation(email: str, code: str, user=Depends(admin_required)):
        return InvitationService.delete_invitation(email, code)
