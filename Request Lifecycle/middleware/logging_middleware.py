import time
from fastapi import Request


async def logging_middleware(request: Request, call_next):
    """Logging middleware to track request execution time.
    
    Logs the HTTP method, path, and execution time for every request.
    This is a cross-cutting concern that applies to all requests.
    """
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    print(
        f"[LOG] {request.method} "
        f"{request.url.path} "
        f"{duration:.4f}s"
    )

    return response