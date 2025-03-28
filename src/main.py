from src.api.invitation.invitation_controller import router as invitation_router
from src.api.auth.auth_controller import router as auth_router
from fastapi import FastAPI
from src.common.database import Database
from mangum import Mangum

# Import migration module/utility

# Run database migrations
Database.run_migration()

app = FastAPI()
app.include_router(invitation_router)
app.include_router(auth_router)

handler = Mangum(app)
