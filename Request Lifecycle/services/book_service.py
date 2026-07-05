from repositories.book_repository import BookRepository


class BookService:
    """Service layer for book business logic.
    
    Responsibilities:
    - Apply business rules
    - Validate business constraints
    - Coordinate repository operations
    - Process data
    
    This layer contains business logic only. No HTTP handling or direct data access.
    """

    def __init__(self):
        self.repo = BookRepository()

    def create_book(self, book: dict) -> dict:
        """Create a new book with business rule validation."""
        print("[SERVICE] create_book called")

        # Business Rule: Price must be greater than zero
        if book["price"] <= 0:
            raise ValueError("Price must be greater than zero")

        # Business Rule: No duplicate books
        existing_book = self.repo.get_by_id(book["id"])
        if existing_book:
            raise ValueError("Book already exists")

        return self.repo.save(book)

    def get_all_books(self, request_id: str, user_id: int, role: str) -> list:
        """Get all books with user context."""
        print(f"[SERVICE] user={user_id} role={role}")
        return self.repo.get_all(request_id)

    def get_book(self, book_id: int) -> dict:
        """Get a specific book by ID."""
        print("[SERVICE] get_book called")
        return self.repo.get_by_id(book_id)

    def delete_book(self, book_id: int) -> dict:
        """Delete a book by ID with validation."""
        print("[SERVICE] delete_book called")
        book = self.repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        return self.repo.delete(book_id)