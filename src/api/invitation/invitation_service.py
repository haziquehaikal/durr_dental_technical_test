# Ensure the module and class exist, or remove the unused import if not needed
from datetime import datetime, timedelta
from src.api.invitation.invitation_repository import InvitationRepository
from src.common.misc_func import MiscFunction
from src.common.models import CreateInvitation, InvitationStatus, CheckInvitationStatus
import uuid


class InvitationService:

    # Create invitation
    def create_invitation(payload: CreateInvitation):

        try:
            # Validate email pattern
            check_email = MiscFunction.validate_email(payload.email)

            # Check if email is valid
            if not check_email:
                return MiscFunction.generate_response("Invalid email format", 400)

            # Check if invitation of this email is already exist and unconfirmed
            # checkInviteThisEmailExist = InvitationRepository.get_invitation_by_email_and_status(
            #     payload.email,
            #     InvitationStatus.UNCONFIRMED.value
            # )

            # if checkInviteThisEmailExist:
            #     return MiscFunction.generate_response("Invitation already exists", 400)

            # Create invitation payload
            response = {
                'id': str(uuid.uuid4()),
                'email': payload.email,
                'code': MiscFunction.generate_code(),
                'status': InvitationStatus.UNCONFIRMED.value,
                'timestamp': datetime.utcnow().isoformat(),
                'expired_at': (datetime.utcnow() + timedelta(days=7)).isoformat(),
            }

            # Save invitation
            result = InvitationRepository.create_invitation(response)

            return MiscFunction.generate_response(response, 201)
        except Exception as e:
            return MiscFunction.generate_response(f"Error creating invitation: {e}", 500)

        # Confirm invitation
    def confirm_invitation(payload: CheckInvitationStatus):
        try:

            print('incoming', payload)

            result = InvitationRepository.get_invitation(
                payload.email, payload.code)

            if result is None:
                return MiscFunction.generate_response("Invitation not found", 404)

            # Check if invitation has been accepted
            if result.get('status') == InvitationStatus.CONFIRMED.value:
                return MiscFunction.generate_response("Invitation has already been accepted", 202)

            # Check if invitation has expired
            expiryDate = result.get('expired_at')
            expiry_datetime = datetime.fromisoformat(expiryDate)
            current_datetime = datetime.utcnow()

            # Do checking
            if current_datetime > expiry_datetime:
                # Update invitation
                # Delete invitation
                InvitationRepository.update_invitation(
                    {"code": payload.code, "email": payload.email},
                    "SET #status = :status",
                    {"#status": "status"},
                    {":status": InvitationStatus.EXPIRED.value}
                )
                return MiscFunction.generates_response("Invitation has expired", 400)

            # Update invitation status
            result = InvitationRepository.update_invitation(
                {"code": payload.code, "email": payload.email},
                "SET #status = :status",
                {"#status": "status"},
                {":status": InvitationStatus.CONFIRMED.value}
            )

            return MiscFunction.generate_response("Invitation confirmed successfully", 202)
        except Exception as e:
            return MiscFunction.generate_response(f"Error comfirming invitation: {e}", 500)

    # Check invitation status
    def check_invitation_status(email: str, code: str):

        try:

            # get invitation detail
            result = InvitationRepository.get_invitation(email, code)

            if result is None:
                return MiscFunction.generate_response("Invitation not found", 404)

            return MiscFunction.generate_response(result, 200)
        except Exception as e:
            return MiscFunction.generate_response(f"Error retriving invitation: {e.response['Error']['Message']}", 500)

    # Delete invitation
    def delete_invitation(email: str, code: str):
        try:

            result = InvitationRepository.get_invitation(email, code)

            if result is None:
                return MiscFunction.generate_response("Invitation not found", 404)

            if result.get('status') != InvitationStatus.UNCONFIRMED.value:
                return MiscFunction.generate_response("Invitation cannot be deleted", 400)

            # Delete invitation
            result = InvitationRepository.update_invitation(
                {"code": code, "email": email},
                "SET #status = :status",
                {"#status": "status"},
                {":status": InvitationStatus.INVALIDATED.value}
            )

            print('result', result)

            response = {
                'email': email,
                'status': InvitationStatus.INVALIDATED.value
            }

            return MiscFunction.generate_response(response, 201)
        except Exception as e:
            return MiscFunction.generate_response(f"Error delete invitation: {e}", 500)
