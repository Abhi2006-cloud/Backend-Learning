from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

from models.user_store import users
from auth.jwt_handler import create_token, verify_token

router = APIRouter()

class LoginRequest(BaseModel):
    username : str
    password : str

@router.post("/jwt/login")
def jwt_login(request: LoginRequest):
    for user in users:
        if (
            user["username"] == request.username
            and user["password"] == request.password
        ):
            token = create_token(user)
            return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )

@router.get("/jwt/profile")
def profile(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization format"
        )

    token = authorization.split(" ")[1]
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload

@router.get("/jwt/admin")
def admin(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization format"
        )

    token = authorization.split(" ")[1]
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    if payload["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return {
        "message": "Welcome Admin!"
    }