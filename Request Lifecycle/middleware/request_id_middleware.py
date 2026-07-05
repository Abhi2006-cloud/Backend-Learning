import uuid
from fastapi import Request


async def request_id_middleware(request: Request, call_next):
    """Request ID middleware for traceability.
    
    Generates a unique request ID for each request and stores it
    in request.state. This enables request tracing across all layers.
    """
    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    print(f"[REQUEST ID] {request_id}")

    response = await call_next(request)

    return response