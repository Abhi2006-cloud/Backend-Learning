"""FastAPI Book Store API - Request Lifecycle Explorer.

This is the entry point of the FastAPI application.
It remains minimal - only bootstrap the application.

Responsibilities:
- Initialize FastAPI app
- Include routers
- Register middleware
- Register exception handlers

Business logic, HTTP handling, and data access belong in their respective layers.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from middleware.logging_middleware import logging_middleware
from middleware.request_id_middleware import request_id_middleware
from middleware.auth_middleware import auth_middleware
from middleware.rate_limit_middleware import rate_limit_middleware
from routers.book_router import router
from exceptions.book_exceptions import (
    BookAlreadyExistsException,
    BookNotFoundException
)

app = FastAPI(title="Book Store API - Request Lifecycle Explorer")


@app.get("/")
def root() -> dict:
    """Root endpoint."""
    return {"message": "Book Store API - Request Lifecycle Explorer"}


# Register middleware (order matters!)
app.middleware("http")(logging_middleware)
app.middleware("http")(request_id_middleware)
app.middleware("http")(auth_middleware)
app.middleware("http")(rate_limit_middleware)

# Include routers
app.include_router(router)


# Exception handlers
@app.exception_handler(BookAlreadyExistsException)
async def book_exists_handler(
    request: Request,
    exc: BookAlreadyExistsException
):
    """Handle BookAlreadyExistsException."""
    return JSONResponse(
        status_code=400,
        content={"error": exc.message}
    )


@app.exception_handler(BookNotFoundException)
async def book_not_found_handler(
    request: Request,
    exc: BookNotFoundException
):
    """Handle BookNotFoundException."""
    return JSONResponse(
        status_code=404,
        content={"error": exc.message}
    )