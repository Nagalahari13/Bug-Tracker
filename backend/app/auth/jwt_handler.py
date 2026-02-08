from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "MYSECRETKEY123"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=5)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
