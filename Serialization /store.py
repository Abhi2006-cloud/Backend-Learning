# TASK 4 — In-memory storage (Python list, no database)

from models.book import Book

authors_db: list[dict] = [
    {"id": 1, "name": "James Clear"},
    {"id": 2, "name": "Robert Kiyosaki"},
]

books_db: list[Book] = [
    Book(
        id=1,
        title="Atomic Habits",
        author="James Clear",
        price=499,
        internal_notes="Bestseller in self-help category",
    ),
    Book(
        id=2,
        title="Rich Dad Poor Dad",
        author="Robert Kiyosaki",
        price=399,
        internal_notes="Finance classic",
    ),
]

