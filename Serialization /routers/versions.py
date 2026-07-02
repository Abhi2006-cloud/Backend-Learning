# TASK 11 — API versioning: /api/v1/books vs /api/v2/books

from fastapi import APIRouter

from models.book import BookResponse, BookResponseV2
from store import books_db

v1_router = APIRouter(prefix="/api/v1/books", tags=["books-v1"])
v2_router = APIRouter(prefix="/api/v2/books", tags=["books-v2"])


@v1_router.get("", response_model=list[BookResponse])
def list_books_v1():
    return [
        BookResponse(
            id=book.id,
            title=book.title,
            author=book.author,
            price=book.price,
        )
        for book in books_db
    ]


@v2_router.get("", response_model=list[BookResponseV2])
def list_books_v2():
    return [
        BookResponseV2(
            id=book.id,
            title=book.title,
            author=book.author,
            price_inr=book.price,
            currency="INR",
        )
        for book in books_db
    ]