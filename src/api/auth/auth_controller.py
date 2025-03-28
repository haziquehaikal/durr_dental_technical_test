from fastapi import APIRouter
from src.api.auth.auth_service import AuthService
from src.common.models import Login

# init router
router = APIRouter(
    prefix="/auth",
    tags=["auth"],

)


class AuthController:

    @router.post("/login", status_code=201)
    def login(payload: Login):
        return AuthService.login(payload)

    @router.get("/logout")
    def logout(email: str, code: str):
        pass
