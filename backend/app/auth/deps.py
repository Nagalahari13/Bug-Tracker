from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database import SessionLocal
from app.models.user import User
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db=Depends(get_db)):
    print("CREDENTIALS RECEIVED", credentials)
    token = credentials.credentials
    print("TOKEN RECEIVED", token)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD DECODE", payload)
        user_id = payload.get("user_id")
    except JWTError as e:
        print("jwt error", e)
        raise HTTPException(status_code=401, detail="Invalid token")
    print("looking for user with id", user_id)
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        print("user not found in db")
        raise HTTPException(status_code=404, detail="User not found")
    print("user found", user.username)
    return user
