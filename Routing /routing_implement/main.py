```python
"""
API Gateway Simulator — FastAPI routing practice file.
"""

from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(title="API Gateway Simulator")


# ── Phase 12: Catch-all for unmatched routes ──

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "Route not found"}
        )

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# ── Phase 1: Static Routes ──

@app.get("/users")
def get_users():
    return {"handler": "users"}


@app.get("/products")
def get_products(
    page: int | None = None,
    limit: int | None = None,
    sort: str | None = None,
    order: str | None = None,
):
    # Phase 5 behavior
    if any(v is not None for v in [page, limit, sort, order]):
        return {
            "page": page,
            "limit": limit,
            "sort": sort,
            "order": order,
        }

    # Phase 1 behavior
    return {"handler": "products"}


@app.get("/orders")
def get_orders():
    return {"handler": "orders"}


# ── Phase 2: Same Path, Different Methods ──

@app.post("/users", status_code=201)
def post_users():
    return {
        "handler": "users",
        "action": "created"
    }


@app.put("/users")
def put_users():
    return {
        "handler": "users",
        "action": "updated"
    }


@app.delete("/users")
def delete_users():
    return {
        "handler": "users",
        "action": "deleted"
    }


# ── Phase 3: Dynamic Routes ──

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"userId": user_id}


# ── Phase 4 + Phase 9: Multiple Dynamic Parameters ──

@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: str, post_id: str):
    return {
        "userId": user_id,
        "postId": post_id
    }


# ── Phase 8 + Final Challenge ──

@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: str,
    page: str | None = None,
    limit: str | None = None
):
    # Final Challenge behavior
    if page is not None or limit is not None:
        return {
            "pathParams": {
                "userId": user_id
            },
            "queryParams": {
                "page": page,
                "limit": limit
            }
        }

    # Phase 8 behavior
    return {
        "userId": user_id,
        "resource": "posts"
    }


# ── Phase 6: Search Endpoint ──

@app.get("/search")
def get_search(query: str):
    return {"query": query}


# ── Phase 7: Pagination Endpoint ──

@app.get("/books")
def get_books(page: int, limit: int):
    return {
        "page": page,
        "limit": limit,
        "totalPages": 50
    }


# ── Phase 10: API Versioning ──

@app.get("/api/v1/products")
def get_products_v1(response: Response):

    response.headers["X-API-Deprecated"] = "true"

    return {
        "warning": "Please migrate to v2",
        "version": "v1",
        "name": "Laptop"
    }


@app.get("/api/v2/products")
def get_products_v2():
    return {
        "version": "v2",
        "title": "Laptop"
    }


# ── Phase 11: Deprecation Warning ──

@app.get("/api/v1/users")
def get_users_v1(response: Response):

    response.headers["X-API-Deprecated"] = "true"

    return {
        "warning": "Please migrate to v2",
        "users": ["John", "Alice"]
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
```
