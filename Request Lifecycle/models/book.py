from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    """Model for creating a new book.
    
    Attributes:
        id: Unique identifier for the book
        title: Title of the book (required)
        price: Price of the book (must be greater than 0)
    """
    id: int
    title: str
    price: float = Field(gt=0, description="Price must be greater than zero")