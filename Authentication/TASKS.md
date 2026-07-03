# Auth Lab API - Task Flow

This document outlines the sequence of tasks for building the authentication laboratory.

## Task Flow

### TASK 1: Create project structure ✅
- [x] Create FastAPI app (main.py)
- [x] Create routers/ directory
- [x] Create auth/ directory
- [x] Create models/ directory
- [x] Add __init__.py files
- [ ] Verify server starts: `uvicorn main:app --reload`
- [ ] Verify Swagger works: http://localhost:8000/docs

**Concept:** Project organization

---

### TASK 2: Create a fake user store
**File to modify:** `models/user_store.py` (create this file)
# TODO: Create in-memory user store
# - Each user needs: id, username, password, role
# - Roles: user, admin
# - At least 3 users required
**Concept:** Identity
**Question:** What information uniquely identifies a user?

---

### TASK 3: Build Username + Password Login
**File to modify:** `routers/auth.py` (create this file)
# TODO: Create POST /login endpoint
# - Validate credentials against user store
# - Return success/failure response
**Concept:** Authentication
**Question:** What question does authentication answer?
**Expected Answer:** "Who are you?"

---

### TASK 4: Implement Session-Based Authentication
**File to modify:** `auth/session_manager.py` (create this file), `routers/auth.py`
# TODO: Add session management to login
# - Generate session ID
# - Store session in memory
# - Associate session with user
**Concepts:** Stateful Authentication, Sessions
**Question:** Why is this called stateful?

---

### TASK 5: Add Cookie Support
**File to modify:** `routers/auth.py`
# TODO: Store session ID in cookie
# - Set cookie on login response
# - Configure cookie settings
**Concepts:** Cookies, Session Cookies
**Observation:** User does not manually send session ID. Browser handles it.
**Question:** What is the job of a cookie?

---

### TASK 6: Protected Route Using Sessions
**File to modify:** `routers/auth.py`
# TODO: Create GET /profile endpoint
# - Read session from cookie
# - Fetch user from session store
# - Return user profile
**Concepts:** Session Validation, Identity Lookup
**Observation:** Server memory is required.

---

### TASK 7: Implement Logout
**File to modify:** `routers/auth.py`
# TODO: Create POST /logout endpoint
# - Remove session from memory
# - Clear cookie
**Concepts:** Session Revocation
**Question:** Why is logout easy with sessions?

---

### TASK 8: Implement JWT Authentication
**File to modify:** `auth/jwt_handler.py` (create this file), `routers/jwt_auth.py` (create this file)
# TODO: Create POST /jwt/login endpoint
# - Generate JWT token
# - Include claims: user_id, role
# - Return token to client
**Concepts:** Stateless Authentication, Claims
**Observation:** No session storage needed.

---

### TASK 9: JWT Protected Route
**File to modify:** `routers/jwt_auth.py`
# TODO: Create GET /jwt/profile endpoint
# - Read JWT from Authorization header
# - Validate signature
# - Extract claims
# - Return user profile
**Concepts:** JWT Validation, Claims Extraction
**Observation:** No database/session lookup required.
**Question:** Why is JWT called self-contained?

---

### TASK 10: Compare Session vs JWT
**File to modify:** `COMPARISON.md` (create this file)
# TODO: Create comparison document
# - Compare: Storage, Scalability, Logout, Complexity
# - Write at least 5 differences
**Concept:** Tradeoffs

---

### TASK 11: Implement API Key Authentication
**File to modify:** `auth/api_key_manager.py` (create this file), `routers/api_routes.py` (create this file)
# TODO: Create API key endpoints
# - POST /generate-api-key
# - GET /api/data (requires API key in header)
**Concepts:** API Keys, Machine-to-Machine Authentication
**Observation:** API Keys identify applications, not users.

---

### TASK 12: Add Roles
**File to modify:** `models/user_store.py` (update existing user store)
# TODO: Ensure roles are stored with users
# - Roles: user, admin
**Concepts:** Authorization
**Question:** What question does authorization answer?
**Expected Answer:** "What can you do?"

---

### TASK 13: Implement RBAC
**File to modify:** `routers/auth.py` (add admin endpoint)
# TODO: Create GET /admin endpoint
# - Only allow admin role
# - Deny access to regular users
**Concepts:** Role Based Access Control (RBAC)
**Observation:** Authentication and authorization are different.

---

### TASK 14: JWT Role Claims
**File to modify:** `auth/jwt_handler.py`, `routers/jwt_auth.py`
# TODO: Store role inside JWT
# - Use JWT claims for authorization decisions
**Concepts:** Claims-Based Authorization
**Observation:** No additional lookup required.

---

### TASK 15: Token Revocation Problem
**File to modify:** No code changes - manual testing scenario
# TODO: Simulate revocation scenario
# 1. User logs in
# 2. JWT issued
# 3. User banned
# 4. Test if JWT still works
**Concept:** JWT Revocation Challenge
**Observation:** Logout is harder with stateless auth.

---

### TASK 16: Hybrid Authentication
**File to modify:** `main.py` (register both routers)
# TODO: Implement both strategies
# - Session Auth for browser routes
# - JWT Auth for API routes
**Concept:** Real-world architecture
**Observation:** Many production systems use hybrid approaches.

---

## FINAL CHALLENGE

Explain the lifecycle of:

### Session Authentication:
Login → Session Created → Cookie Sent → Cookie Returned → Session Lookup → User Identified

### JWT Authentication:
Login → JWT Created → JWT Sent → JWT Returned → Signature Verified → Claims Read → User Identified

### Authorization:
User Identified → Role Checked → Permission Granted/Denied

**If you cannot explain these flows without looking at notes, the project is incomplete.**
