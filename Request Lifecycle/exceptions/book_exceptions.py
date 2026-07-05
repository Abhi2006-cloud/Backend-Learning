"""Custom exceptions for the book API."""


class BookAlreadyExistsException(Exception):
    """Exception raised when attempting to create a duplicate book."""

    def __init__(self, message="Book already exists"):
        self.message = message


class BookNotFoundException(Exception):
    """Exception raised when a book is not found."""

    def __init__(self, message="Book not found"):
        self.message = message

