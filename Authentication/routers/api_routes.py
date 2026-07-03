from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

from auth.api_key_manager import generate_api_key, validate_api_key

router = APIRouter()

class AppRequest(BaseModel):
    app_name: str

@router.post("/generate-api-key")
def generate_api_key_endpoint(request: AppRequest):
    key = generate_api_key(request.app_name)
    return {
        "api_key": key
    }

@router.get("/api/data")
def get_data(x_api_key: str = Header(None)):
    app = validate_api_key(x_api_key)

    if app is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return {
        "message": "Access granted",
        "application": app
    }