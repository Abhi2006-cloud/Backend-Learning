# FastAPI Request Lifecycle Explorer

A production-grade FastAPI project demonstrating layered architecture, request lifecycle, and separation of concerns. This project is designed to teach how real-world FastAPI applications are structured.

## 🎯 Project Goal

Build a Book Store API whose real purpose is to understand:
- Request Lifecycle
- Handler Layer
- Service Layer
- Repository Layer
- Middleware
- Request Context
- Logging
- Authentication
- Error Handling
- Layered Architecture
- Separation of Concerns

## 🏗️ Architecture

```
Client Request
    ↓
Middleware Layer (Cross-Cutting Concerns)
    ↓
Router Layer (Handler Layer)
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
Repository Response
    ↓
Service Response
    ↓
Handler Response
    ↓
Middleware Response
    ↓
Client Response
```

## 📁 Project Structure

```
Request Lifecycle/
├── app/                          # Application container
├── routers/                      # Handler Layer (HTTP operations)
│   ├── __init__.py
│   └── book_router.py
├── services/                     # Service Layer (Business Logic)
│   ├── __init__.py
│   └── book_service.py
├── repositories/                 # Repository Layer (Data Access)
│   ├── __init__.py
│   └── book_repository.py
├── middleware/                   # Middleware Layer (Cross-Cutting Concerns)
│   ├── __init__.py
│   ├── logging_middleware.py
│   ├── request_id_middleware.py
│   ├── auth_middleware.py
│   └── rate_limit_middleware.py
├── models/                       # Data Models
│   └── book.py
├── exceptions/                   # Custom Exceptions
│   └── book_exceptions.py
├── main.py                       # Application Entry Point
├── tasks.md                      # Task List
├── REQUEST_FLOW_DIAGRAM.md       # Request Flow Documentation
├── MIDDLEWARE_ORDER_EXPERIMENT.md # Middleware Order Analysis
├── ARCHITECTURE_AUDIT.md        # Architecture Audit Results
└── FINAL_CHALLENGE_LIFECYCLE_TRACE.md # Complete Lifecycle Trace
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or poetry

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Request Lifecycle
```

2. Install dependencies:
```bash
pip install fastapi uvicorn pydantic
```

### Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Swagger UI

Access the interactive API documentation at:
```
http://localhost:8000/docs
```

## 🔑 API Authentication

All API endpoints (except public paths) require an `X-API-Key` header.

### Valid API Keys

- `valid-key-123` (Admin user, user_id: 1)
- `valid-key-456` (Regular user, user_id: 2)

### Example Request

```bash
curl -X POST http://localhost:8000/books \
  -H "X-API-Key: valid-key-123" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Clean Code", "price": 29.99}'
```

## 📚 API Endpoints

### Books

- `POST /books` - Create a new book
- `GET /books` - Get all books (with optional sort parameter)
- `GET /books/{book_id}` - Get a specific book
- `DELETE /books/{book_id}` - Delete a book

### Example Requests

**Create a book:**
```bash
curl -X POST http://localhost:8000/books \
  -H "X-API-Key: valid-key-123" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Clean Code", "price": 29.99}'
```

**Get all books:**
```bash
curl -X GET http://localhost:8000/books \
  -H "X-API-Key: valid-key-123"
```

**Get a specific book:**
```bash
curl -X GET http://localhost:8000/books/1 \
  -H "X-API-Key: valid-key-123"
```

**Delete a book:**
```bash
curl -X DELETE http://localhost:8000/books/1 \
  -H "X-API-Key: valid-key-123"
```

## 🏛️ Layer Responsibilities

### Handler Layer (Routers)
- **Responsibility:** HTTP-specific operations
- **What it does:** Receive requests, validate input, call services, return responses
- **What it does NOT do:** Business logic, data access

### Service Layer
- **Responsibility:** Business logic and orchestration
- **What it does:** Apply business rules, coordinate repositories, process data
- **What it does NOT do:** HTTP handling, direct data access

### Repository Layer
- **Responsibility:** Data access only
- **What it does:** Store, fetch, delete data
- **What it does NOT do:** Business logic, business validation

### Middleware Layer
- **Responsibility:** Cross-cutting concerns
- **What it does:** Logging, authentication, rate limiting, request ID generation
- **What it does NOT do:** Business logic, route-specific logic

## 🔍 Key Features

### Request Lifecycle Tracing
Every request is assigned a unique ID that flows through all layers, enabling complete traceability.

### Authentication
API key-based authentication with user context storage.

### Rate Limiting
5 requests per minute per user to prevent abuse.

### Request Transformation
Automatic parameter transformation (e.g., default sort values).

### Global Error Handling
Consistent JSON error responses across all endpoints.

### Comprehensive Logging
Request logging with execution time tracking.

## 📖 Learning Resources

- [REQUEST_FLOW_DIAGRAM.md](REQUEST_FLOW_DIAGRAM.md) - Complete request flow documentation
- [MIDDLEWARE_ORDER_EXPERIMENT.md](MIDDLEWARE_ORDER_EXPERIMENT.md) - Middleware ordering analysis
- [ARCHITECTURE_AUDIT.md](ARCHITECTURE_AUDIT.md) - Architecture audit results
- [FINAL_CHALLENGE_LIFECYCLE_TRACE.md](FINAL_CHALLENGE_LIFECYCLE_TRACE.md) - Step-by-step lifecycle trace
- [tasks.md](tasks.md) - Complete task list with progress tracking

## 🎓 Concepts Taught

- **Handler Layer:** Request parsing, validation, response creation
- **Service Layer:** Business logic, orchestration
- **Repository Layer:** Data access
- **Middleware:** Logging, authentication, rate limiting, error handling
- **Request Context:** User ID, roles, request IDs
- **Architecture:** Separation of concerns, request lifecycle, production backend structure

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

This is a learning project. Feel free to fork and modify for your own learning.

## 📧 Contact

For questions or suggestions, please open an issue in the repository.
