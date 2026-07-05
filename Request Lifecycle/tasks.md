# FastAPI Request Lifecycle Explorer - Task List

## TASK 1: Create Project Structure ✅
- [x] Create directory structure: app/, routers/, services/, repositories/, middleware/, models/
- [x] Create main.py with minimal FastAPI setup
- [x] Verify FastAPI starts successfully
- [x] Verify Swagger UI works at http://localhost:8000/docs

**Concepts:** Project Structure, Layer Separation

---

## TASK 2: Create a Request Flow Diagram ✅
- [x] Draw the request flow diagram showing:
  - Request → Middleware → Handler → Service → Repository → Response
- [x] Document responsibility of each layer
- [x] Explain what each layer does
- [x] Created REQUEST_FLOW_DIAGRAM.md

**Concepts:** Request Lifecycle, Layer Responsibilities

---

## TASK 3: Create Book Repository ✅
- [x] Create repositories/book_repository.py
- [x] Implement: store books, fetch books, delete books
- [x] Ensure repository only deals with data (no business logic)
- [x] Use in-memory storage (dictionary or list)

**Concepts:** Repository Layer, Data Access Layer

---

## TASK 4: Create Book Service ✅
- [x] Create services/book_service.py
- [x] Implement business rules (prevent duplicates, check price rules)
- [x] Coordinate between repository operations
- [x] Ensure repository never called directly from routes

**Concepts:** Service Layer, Business Logic

---

## TASK 5: Create Book Handler ✅
- [x] Create routers/book_router.py
- [x] Implement POST /books endpoint
- [x] Implement GET /books endpoint
- [x] Handlers should: receive request, validate input, call service, return response
- [x] No business logic in handlers

**Concepts:** Handler Layer, HTTP Layer

---

## TASK 6: Observe Full Lifecycle ✅
- [x] Add logging statements in middleware
- [x] Add logging statements in handlers
- [x] Add logging statements in services
- [x] Add logging statements in repositories
- [x] Make one request and observe complete flow in logs

**Concepts:** Request Lifecycle

---

## TASK 7: Request Validation ✅
- [x] Create models/book.py with Pydantic models
- [x] Add validation: title required, price > 0
- [x] Ensure invalid requests fail before reaching service layer

**Concepts:** Validation, Deserialization

---

## TASK 8: Request Transformation ✅
- [x] In handler, check if sort parameter is missing
- [x] If missing, automatically set sort = "date"
- [x] Transform request before service call

**Concepts:** Transformation Layer

---

## TASK 9: Logging Middleware ✅
- [x] Create middleware/logging_middleware.py
- [x] Log: path, method, execution time
- [x] Ensure every request is logged

**Concepts:** Logging Middleware, Cross-Cutting Concerns

---

## TASK 10: Request ID Middleware ✅
- [x] Create middleware/request_id_middleware.py
- [x] Generate unique request ID
- [x] Store in request context
- [x] Ensure every request gets unique ID

**Concepts:** Request Context, Traceability

---

## TASK 11: Use Request Context ✅
- [x] Store request_id in context
- [x] Access request_id from middleware
- [x] Access request_id from handlers
- [x] Access request_id from services
- [x] Verify same request ID visible across layers

**Concepts:** Request Scoped Data, Context Sharing

---

## TASK 12: Authentication Middleware ✅
- [x] Create middleware/auth_middleware.py
- [x] Check X-API-Key header
- [x] Reject request if key missing
- [x] Continue if key valid

**Concepts:** Authentication Middleware

---

## TASK 13: Store User Information in Context ✅
- [x] In auth middleware, store user_id and role in request context
- [x] Ensure handlers can access user information

**Concepts:** Request Context, Auth Context

---

## TASK 14: Rate Limiting Middleware ✅
- [x] Create middleware/rate_limit_middleware.py
- [x] Allow 5 requests per minute
- [x] 6th request should return 429 Too Many Requests

**Concepts:** Rate Limiting Middleware

---

## TASK 15: Global Error Handling ✅
- [x] Create custom exception
- [x] Trigger exception from service layer
- [x] Create global error handler middleware
- [x] Ensure client receives consistent JSON error response

**Concepts:** Global Error Middleware, Exception Handling

---

## TASK 16: Middleware Order Experiment ✅
- [x] Test middleware order: Logging → Auth
- [x] Test middleware order: Auth → Logging
- [x] Observe behavior differences
- [x] Document why order matters
- [x] Created MIDDLEWARE_ORDER_EXPERIMENT.md

**Concepts:** Middleware Ordering

---

## TASK 17: Architecture Audit ✅
- [x] Review every file
- [x] Verify Handler: HTTP only
- [x] Verify Service: Business logic only
- [x] Verify Repository: Data access only
- [x] Verify Middleware: Cross-cutting concerns only
- [x] Ensure no responsibility leakage
- [x] Created ARCHITECTURE_AUDIT.md

**Concepts:** Separation of Concerns, Single Responsibility Principle

---

## FINAL CHALLENGE: Trace Complete Request Lifecycle ✅
- [x] Trace POST /books request completely
- [x] For every step explain:
  1. What layer is running?
  2. What responsibility does it have?
  3. What data is available?
  4. Why does this layer exist?
- [x] Verify you can explain entire lifecycle without looking at notes
- [x] Created FINAL_CHALLENGE_LIFECYCLE_TRACE.md

**Concepts:** Complete Request Lifecycle Understanding
