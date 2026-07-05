# In-memory database for demonstration purposes
books_db = {}


class BookRepository:
    """Repository layer for book data access operations.
    
    Responsibilities:
    - Store books
    - Fetch books
    - Delete books
    
    This layer only deals with data access. No business logic.
    """

    def save(self, book: dict) -> dict:
        """Save a book to the database."""
        print("[REPOSITORY] save called")
        books_db[book["id"]] = book
        return book

    def get_all(self, request_id: str) -> list:
        """Get all books from the database."""
        print(f"[REPOSITORY] get_all called with request_id: {request_id}")
        return list(books_db.values())

    def get_by_id(self, book_id: int) -> dict:
        """Get a specific book by ID."""
        print(f"[REPOSITORY] get_by_id({book_id})")
        return books_db.get(book_id)

    def delete(self, book_id: int) -> dict:
        """Delete a book by ID."""
        print(f"[REPOSITORY] delete({book_id})")
        return books_db.pop(book_id, None)