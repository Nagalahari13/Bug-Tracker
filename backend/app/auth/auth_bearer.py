from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.auth_handler import decodeJWT

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if not credentials:
            raise HTTPException(status_code=403, detail="Invalid authorization")
        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=403, detail="Invalid token scheme")
        return credentials.credentials

# ✔✔ THIS IS THE REAL FIX (You were missing this)
def get_current_user(token: str = Depends(JWTBearer())):
    user = decodeJWT(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user
