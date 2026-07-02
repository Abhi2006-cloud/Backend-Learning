# TASK 1  — Project structure + application entry point
# TASK 14 — Catch-all route (must be registered last)

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routers.authors import router as authors_router
from routers.books import router as books_router
from routers.health import router as health_router
from routers.versions import v1_router, v2_router

app = FastAPI(
    title="Library Catalog API",
    description="FastAPI learning project for routing, serialization, and validation",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(books_router)
app.include_router(authors_router)
app.include_router(v1_router)
app.include_router(v2_router)


@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def catch_all(full_path: str, request: Request):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Route not found",
            "path": f"/{full_path}",
            "method": request.method,
        },
    )

