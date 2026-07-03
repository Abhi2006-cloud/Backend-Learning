from fastapi import FastAPI
from routers import auth, jwt_auth, api_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" :"World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(auth.router)
app.include_router(jwt_auth.router)
app.include_router(api_routes.router)
