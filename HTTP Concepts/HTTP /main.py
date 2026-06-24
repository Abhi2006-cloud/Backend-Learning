from pathlib import Path

from fastapi import FastAPI, File, Header, HTTPException, Request, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI(title="HTTP Inspector API")

# TODO (Endpoint 8 — CORS):
# Add CORSMiddleware to app with allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
# Test: curl -D - -H "Origin: http://localhost:3000" http://127.0.0.1:8000/inspect
# Concepts: Origin, Access-Control-Allow-Origin, Preflight Request


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

CACHE_DATA = {"message": "Hello"}
CACHE_ETAG = '"v1"'


@app.get("/inspect")
def inspect(request: Request):
    return{
        "method" : request.method,
        "headers" : dict(request.headers),
        "query" : dict(request.query_params),
        "ip" : request.client.host
    }




@app.get("/profile")
def profile(authorization: str | None = Header(default=None)):
    
    if authorization != "Bearer secret123":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "message": "Authenticated — every request carries its own identity"
    }


@app.get("/resource")
def resource_get():
    return {"method": "GET"}

@app.post("/resource", status_code=201)
def resource_post():
    return {"method": "POST"}


@app.put("/resource")
def resource_put():
   return {"method": "PUT"}


@app.patch("/resource")
def resource_patch():
    return {"method": "PATCH"}


@app.delete("/resource")
def resource_delete():
        return {"method": "DELETE"}


@app.get("/status/{code}")
def status_lab(code: int):
    if code < 100 or 600 > code:
        raise HTTPException(status_code=400, detail="Invalid status code")
    else:
        return JSONResponse(status_code=code, content={"status": code})


@app.get("/cache")
def cache_demo(request: Request):

    client_etag = request.headers.get("If-None-Match")

    if client_etag == CACHE_ETAG:
        return Response(status_code=304)

    return JSONResponse(
        content=CACHE_DATA,
        headers={
            "ETag": CACHE_ETAG,
            "Cache-Control": "max-age=3600"
        }
    )

@app.get("/user")
def user(accept: str | None = Header(default="application/json")):

    if "text/plain" in accept:
        return PlainTextResponse("name=John Doe")

    return {
        "name": "John Doe",
        "email": "john@example.com"
    }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    file_bytes = await file.read()
    save_path = UPLOAD_DIR / file.filename
    with open(save_path, "wb") as f:
        f.write(file_bytes)
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(file_bytes),
        "saved_to": str(save_path)
    }