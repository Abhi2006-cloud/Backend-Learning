from fastapi import Request
from fastapi.responses import JSONResponse

# Valid API keys for demonstration
API_KEYS = {
    "valid-key-123": {"user_id": 1, "role": "admin"},
    "valid-key-456": {"user_id": 2, "role": "user"}
}


async def auth_middleware(request: Request, call_next):
    """Authentication middleware to validate API keys.
    
    Validates the X-API-Key header and stores user context (user_id, role)
    in request.state. Public paths (/, /docs, /openapi.json, /favicon.ico)
    are exempt from authentication.
    """
    # Skip authentication for public paths
    public_paths = ["/", "/docs", "/openapi.json", "/favicon.ico"]
    if request.url.path in public_paths:
        return await call_next(request)

    api_key = request.headers.get("X-API-Key")
    user = API_KEYS.get(api_key)

    if not user:
        return JSONResponse(
            status_code=401,
            content={"message": "Unauthorized"}
        )

    request.state.user_id = user["user_id"]
    request.state.role = user["role"]

    return await call_next(request)

