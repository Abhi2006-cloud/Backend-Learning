from fastapi import Request
from fastapi.responses import JSONResponse
import time

# In-memory request tracker for rate limiting
request_tracker = {}

# Rate limit configuration
RATE_LIMIT = 5  # requests per minute
WINDOW_SECONDS = 60  # time window in seconds


async def rate_limit_middleware(request: Request, call_next):
    """Rate limiting middleware to prevent API abuse.
    
    Enforces a rate limit of 5 requests per minute per user.
    Returns 429 Too Many Requests when limit is exceeded.
    """
    user_id = getattr(request.state, "user_id", None)

    # Skip rate limiting if no user_id (public paths)
    if not user_id:
        return await call_next(request)

    now = time.time()

    # Get user's request history
    user_requests = request_tracker.get(user_id, [])

    # Filter requests within the time window
    user_requests = [
        ts
        for ts in user_requests
        if now - ts < WINDOW_SECONDS
    ]

    # Check if rate limit exceeded
    if len(user_requests) >= RATE_LIMIT:
        return JSONResponse(
            status_code=429,
            content={
                "message": "Too Many Requests"
            }
        )

    # Add current request to history
    user_requests.append(now)
    request_tracker[user_id] = user_requests

    return await call_next(request)