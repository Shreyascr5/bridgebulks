import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Read SECRET_KEY from environment - NEVER hardcode in production.
# Set this in your Render backend environment variables.
SECRET_KEY = os.getenv("SECRET_KEY", "changeme-set-SECRET_KEY-in-render-env")
ALGORITHM = "HS256"

security = HTTPBearer(auto_error=False)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=10)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    if not credentials:
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
