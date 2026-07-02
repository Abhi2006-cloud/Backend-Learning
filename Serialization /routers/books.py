# TASK 4 — POST /books (request body + JSON deserialization)
# TASK 5 — GET /books (serialization to JSON)
# TASK 6 — GET /books/{book_id} (path parameter)
# TASK 7 — Pagination (?page=1&limit=10)
# TASK 8 — GET /books/search?query=...

from fastapi import APIRouter, HTTPException, Query

from models.book import Book, BookCreate, BookResponse
from store import books_db

router = APIRouter(prefix="/books", tags=["books"])


def _paginate(items: list, page: int, limit: int) -> list:
    start = (page - 1) * limit
    end = start + limit
    return items[start:end]


def _to_response(book: Book) -> BookResponse:
    return BookResponse(
        id=book.id,
        title=book.title,
        author=book.author,
        price=book.price,
    )


@router.post("", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate):
    if any(existing.id == book.id for existing in books_db):
        raise HTTPException(status_code=409, detail="Book with this id already exists")

    new_book = Book(**book.model_dump(), internal_notes="Added via API")
    books_db.append(new_book)
    return _to_response(new_book)


@router.get("", response_model=list[BookResponse])
def list_books(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    paginated = _paginate(books_db, page, limit)
    return [_to_response(book) for book in paginated]


@router.get("/search", response_model=list[BookResponse])
def search_books(query: str = Query(..., min_length=1)):
    query_lower = query.lower()
    results = [
        book
        for book in books_db
        if query_lower in book.title.lower() or query_lower in book.author.lower()
    ]
    return [_to_response(book) for book in results]


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return _to_response(book)

    raise HTTPException(status_code=404, detail="Book not found") 

