# TASK 9  — GET /authors/{author_id}/books
# TASK 10 — GET /authors/{author_id}/books/{book_id}

from fastapi import APIRouter, HTTPException

from models.book import BookResponse
from store import authors_db, books_db

router = APIRouter(prefix="/authors", tags=["authors"])


def _get_author_name(author_id: int) -> str:
    for author in authors_db:
        if author["id"] == author_id:
            return author["name"]

    raise HTTPException(status_code=404, detail="Author not found")


def _to_response(book) -> BookResponse:
    return BookResponse(
        id=book.id,
        title=book.title,
        author=book.author,
        price=book.price,
    )


@router.get("/{author_id}/books", response_model=list[BookResponse])
def list_author_books(author_id: int):
    author_name = _get_author_name(author_id)
    author_books = [book for book in books_db if book.author == author_name]
    return [_to_response(book) for book in author_books]


@router.get("/{author_id}/books/{book_id}", response_model=BookResponse)
def get_author_book(author_id: int, book_id: int):
    author_name = _get_author_name(author_id)

    for book in books_db:
        if book.id == book_id and book.author == author_name:
            return _to_response(book)

    raise HTTPException(status_code=404, detail="Book not found for this author")