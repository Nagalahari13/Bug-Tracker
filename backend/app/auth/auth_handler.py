from datetime import datetime, timedelta
from jose import jwt
import time

SECRET = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str):
    payload = {
        "id": user_id,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token_response(token)

def decodeJWT(token: str):
    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return decoded if decoded["expires"] >= time.time() else None
    except:
        return None
