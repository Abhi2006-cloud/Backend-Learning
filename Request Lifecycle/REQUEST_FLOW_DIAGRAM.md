# Request Flow Diagram

## Complete Request Lifecycle

```
CLIENT REQUEST
    ↓
┌─────────────────────────────────────────────────────────────┐
│  MIDDLEWARE LAYER (Cross-Cutting Concerns)                  │
│  1. Request ID Middleware - Generate unique request_id     │
│  2. Authentication Middleware - Validate X-API-Key         │
│  3. Rate Limiting Middleware - Check rate limits            │
│  4. Logging Middleware - Log request start                 │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│  ROUTER LAYER (Handler Layer)                               │
│  - Receive HTTP request                                      │
│  - Validate input using Pydantic models                     │
│  - Transform request parameters                             │
│  - Extract context data (request_id, user_id, role)         │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│  SERVICE LAYER (Business Logic)                             │
│  - Apply business rules                                      │
│  - Validate business constraints                             │
│  - Coordinate repository operations                          │
│  - Process data                                              │
└─────────────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────────────┐
│  REPOSITORY LAYER (Data Access)                             │
│  - Store data                                                 │
│  - Fetch data                                                 │
│  - Delete data                                                │
└─────────────────────────────────────────────────────────────┘
    ↓
REPOSITORY RESPONSE
    ↓
SERVICE RESPONSE (with business logic applied)
    ↓
HANDLER RESPONSE (HTTP formatted)
    ↓
┌─────────────────────────────────────────────────────────────┐
│  MIDDLEWARE LAYER (Response Path)                           │
│  - Logging Middleware - Log execution time                   │
└─────────────────────────────────────────────────────────────┘
    ↓
CLIENT RESPONSE
```

## Layer Responsibilities

### 1. Middleware Layer
**Responsibility:** Cross-cutting concerns that apply to ALL requests
- **Request ID Middleware:** Generate unique request_id for traceability
- **Authentication Middleware:** Validate API keys, extract user info
- **Rate Limiting Middleware:** Prevent abuse, enforce limits
- **Logging Middleware:** Track request execution time and paths

**What NOT to do:**
- Business logic
- Route-specific operations
- Data access

### 2. Router/Handler Layer
**Responsibility:** HTTP-specific operations
- Parse HTTP requests
- Validate input using Pydantic models
- Transform request parameters (e.g., default values)
- Extract context data from request.state
- Call service layer
- Format HTTP responses

**What NOT to do:**
- Business logic
- Direct data access
- Email sending, file operations

### 3. Service Layer
**Responsibility:** Business logic and orchestration
- Apply business rules (e.g., price > 0, no duplicates)
- Validate business constraints
- Coordinate multiple repository operations
- Process and transform data
- Raise business exceptions

**What NOT to do:**
- HTTP-specific logic
- Direct database queries (use repositories)
- Input validation (that's handler's job)

### 4. Repository Layer
**Responsibility:** Data access only
- Store data
- Fetch data
- Delete data
- Data persistence operations

**What NOT to do:**
- Business logic
- Business rule validation
- Email sending
- Any operations beyond data access

## Data Flow Example: POST /books

1. **Client** sends POST /books with JSON body
2. **Request ID Middleware** generates request_id, stores in request.state
3. **Authentication Middleware** validates X-API-Key, stores user_id and role in request.state
4. **Rate Limiting Middleware** checks if user exceeded 5 requests/minute
5. **Logging Middleware** logs request start
6. **Handler** validates BookCreate model (title required, price > 0)
7. **Handler** calls service.create_book(book.model_dump())
8. **Service** checks if price > 0 (business rule)
9. **Service** checks if book already exists (business rule)
10. **Service** calls repository.save(book)
11. **Repository** stores book in in-memory dictionary
12. **Repository** returns book
13. **Service** returns book
14. **Handler** returns book as JSON response
15. **Logging Middleware** logs execution time
16. **Client** receives JSON response

## Key Concepts

- **Separation of Concerns:** Each layer has one clear responsibility
- **Single Responsibility Principle:** No layer does more than it should
- **Request Context:** Data shared across layers via request.state
- **Traceability:** request_id allows tracking request through all layers
- **Cross-Cutting Concerns:** Middleware handles concerns that apply to all requests
