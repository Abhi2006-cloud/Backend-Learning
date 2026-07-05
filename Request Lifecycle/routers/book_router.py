from fastapi import APIRouter, Request
from services.book_service import BookService
from models.book import BookCreate

router = APIRouter()
service = BookService()


@router.post("/books")
def create_book(book: BookCreate) -> dict:
    """Create a new book.
    
    Handler layer responsibilities:
    - Receive HTTP request
    - Validate input using Pydantic model
    - Call service layer
    - Return HTTP response
    """
    print("[ROUTER] create_book endpoint called")
    return service.create_book(book.model_dump())


@router.get("/books")
def get_books(request: Request, sort: str = None) -> list:
    """Get all books with optional sorting.
    
    Request transformation: If sort parameter is missing,
    automatically set it to "date".
    """
    # Request transformation
    if sort is None:
        sort = "date"
    
    request_id = request.state.request_id
    user_id = request.state.user_id
    role = request.state.role

    print(f"[ROUTER] user={user_id} role={role} sort={sort}")

    return service.get_all_books(request_id, user_id, role)


@router.get("/books/{book_id}")
def get_book(book_id: int) -> dict:
    """Get a specific book by ID."""
    print("[ROUTER] get_book endpoint called")
    return service.get_book(book_id)


@router.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    """Delete a book by ID."""
    print("[ROUTER] delete_book endpoint called")
    return service.delete_book(book_id)
