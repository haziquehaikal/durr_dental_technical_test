
from pydantic import BaseModel
from enum import Enum

# Enum class for invitation status


class InvitationStatus(Enum):
    UNCONFIRMED = "unconfirmed"
    CONFIRMED = "confirmed"
    EXPIRED = "expired"
    INVALIDATED = "invalidated"


class CreateInvitation(BaseModel):
    email: str


class CreateInvitationRes(BaseModel):
    email: str
    first_name: str
    last_name: str


class CheckInvitationStatus(CreateInvitation):
    code: str


class Login(CreateInvitation):
    password: str
