from fastapi import APIRouter, HTTPException , Response , Request
from pydantic import BaseModel

from models.user_store import users
from auth.session_manager import create_session, get_user
from auth.session_manager import delete_session
router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(request: LoginRequest , response: Response):

    for user in users:
        if (
            user["username"] == request.username
            and user["password"] == request.password
        ):
            session_id = create_session(user)

            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True,
                max_age=3600,
            )

            return {
                "message": "Login Successful"
            }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )

@router.get("/profile")
def get_profile(request : Request):

    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
    
    #Find user by session
    user  = get_user(session_id)
    if not user:
        raise HTTPException(
            status_code = 401,
            detail="Invalid session"
        )
    
    return {
        "id": user["id"],
        "username": user["username"],
        "role": user["role"]
    }

@router.post("/logout")
def logout(request: Request , response: Response):
    session_id = request.cookies.get("session_id")
    if(session_id):
        delete_session(session_id)

    response.delete_cookie("session_id")
    return {
        "message" : "Logout Successful"
    }

@router.get("/admin")
def admin(request : Request):

    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(
            status_code = 401,
            detail = "Not authenticated"
        )
        
    user = get_user(session_id)

    if not user :
        raise HTTPException(
            status_code = 401,
            detail = "Invalid session"
        )

    if user["role"] != "admin":
        raise HTTPException(
            status_code = 403,
            detail = "Access denied"
        )

    return {
        "message": "Admin access granted"
    }
    

