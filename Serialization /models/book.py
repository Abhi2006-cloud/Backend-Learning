# TASK 3 — Book Pydantic model (deserialization + validation)
# TASK 12 — Response models hide internal fields (internal_notes)
# TASK 13 — Invalid payloads trigger 422 via Field constraints

from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    id: int
    title: str
    author: str
    price: float = Field(gt=0)


class Book(BookCreate):
    internal_notes: str = ""


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float


class BookResponseV2(BaseModel):
    id: int
    title: str
    author: str
    price_inr: float
    currency: str = "INR"
