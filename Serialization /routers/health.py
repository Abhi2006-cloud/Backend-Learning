# TASK 2 — Static route: GET /health
# TODO: Implement this endpoint


from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return {
        "status": "ok"
    }
