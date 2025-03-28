from fastapi import FastAPI, Request, HTTPException

# Admin-only check


async def admin_required(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if token != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return token
