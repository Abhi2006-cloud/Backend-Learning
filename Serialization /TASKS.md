# Library Catalog API — Task → Code Map

Each task below shows the exact code that implements it.

---

## TASK 1 — Project Structure

**Files:** `main.py`, `routers/`, `models/`, `requirements.txt`

```python
# main.py
from fastapi import FastAPI

from routers.authors import router as authors_router
from routers.books import router as books_router
from routers.health import router as health_router
from routers.versions import v1_router, v2_router

app = FastAPI(title="Library Catalog API")

app.include_router(health_router)
app.include_router(books_router)
app.include_router(authors_router)
app.include_router(v1_router)
app.include_router(v2_router)
```

```txt
# requirements.txt
fastapi>=0.115.0
uvicorn>=0.32.0
```

**Run:** `uvicorn main:app --reload` → open `/docs`

---

## TASK 2 — GET /health

**File:** `routers/health.py`

```python
from fastapi import APIRouter

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return {"status": "ok"}
```

---

## TASK 3 — Book Pydantic Model

**File:** `models/book.py`

```python
from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    price: float = Field(gt=0)

class Book(BookCreate):
    internal_notes: str = ""
```

---

## TASK 4 — POST /books

**Files:** `routers/books.py`, `store.py`

```python
# store.py
books_db: list[Book] = [...]

# routers/books.py
@router.post("", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate):
    new_book = Book(**book.model_dump(), internal_notes="Added via API")
    books_db.append(new_book)
    return _to_response(new_book)
```

---

## TASK 5 — GET /books

**File:** `routers/books.py`

```python
@router.get("", response_model=list[BookResponse])
def list_books(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    paginated = _paginate(books_db, page, limit)
    return [_to_response(book) for book in paginated]
```

---

## TASK 6 — GET /books/{book_id}

**File:** `routers/books.py`

```python
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return _to_response(book)
    raise HTTPException(status_code=404, detail="Book not found")
```

---

## TASK 7 — Pagination

**File:** `routers/books.py`

```python
def _paginate(items: list, page: int, limit: int) -> list:
    start = (page - 1) * limit
    end = start + limit
    return items[start:end]

# Used in list_books via ?page=1&limit=10
```

---

## TASK 8 — Search

**File:** `routers/books.py`

```python
@router.get("/search", response_model=list[BookResponse])
def search_books(query: str = Query(..., min_length=1)):
    query_lower = query.lower()
    results = [
        book for book in books_db
        if query_lower in book.title.lower() or query_lower in book.author.lower()
    ]
    return [_to_response(book) for book in results]
```

---

## TASK 9 — Nested Routes (author → books)

**File:** `routers/authors.py`

```python
@router.get("/{author_id}/books", response_model=list[BookResponse])
def list_author_books(author_id: int):
    author_name = _get_author_name(author_id)
    author_books = [book for book in books_db if book.author == author_name]
    return [_to_response(book) for book in author_books]
```

---

## TASK 10 — Deep Nested Routes

**File:** `routers/authors.py`

```python
@router.get("/{author_id}/books/{book_id}", response_model=BookResponse)
def get_author_book(author_id: int, book_id: int):
    author_name = _get_author_name(author_id)
    for book in books_db:
        if book.id == book_id and book.author == author_name:
            return _to_response(book)
    raise HTTPException(status_code=404, detail="Book not found for this author")
```

---

## TASK 11 — API Versioning

**File:** `routers/versions.py`

```python
v1_router = APIRouter(prefix="/api/v1/books", tags=["books-v1"])
v2_router = APIRouter(prefix="/api/v2/books", tags=["books-v2"])

@v1_router.get("", response_model=list[BookResponse])
def list_books_v1(): ...

@v2_router.get("", response_model=list[BookResponseV2])
def list_books_v2(): ...  # returns price_inr + currency
```

---

## TASK 12 — Response Models

**File:** `models/book.py`

```python
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float
    # internal_notes is NOT included — hidden from clients
```

---

## TASK 13 — Validation Errors (422)

**File:** `models/book.py`

```python
class BookCreate(BaseModel):
    id: int
    title: str        # missing → 422
    author: str
    price: float = Field(gt=0)  # missing or <= 0 → 422
```

**Test:**

```bash
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{"id":4,"title":"","author":"Test"}'
# → 422 Unprocessable Entity
```

---

## TASK 14 — Catch-All Route

**File:** `main.py` (registered last)

```python
@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def catch_all(full_path: str, request: Request):
    return JSONResponse(
        status_code=404,
        content={"error": "Route not found", "path": f"/{full_path}", "method": request.method},
    )
```

---

## FINAL CHALLENGE — POST /books Request Trace

```
POST /books
{"id":1,"title":"Atomic Habits","author":"James Clear","price":499}
```

1. **Route matching** — FastAPI matches `POST` + path `/books` to `create_book` in `routers/books.py`.
2. **Deserialization** — JSON body is parsed into a `BookCreate` Pydantic object.
3. **Validation** — Pydantic checks types; `price > 0`, required fields present. Fail → 422.
4. **Handler execution** — `Book(**book.model_dump())` is appended to `books_db`.
5. **Serialization** — Return value is converted via `BookResponse` (strips `internal_notes`).
6. **Response generation** — FastAPI returns `201` + JSON `{"id":1,"title":"Atomic Habits",...}`.
