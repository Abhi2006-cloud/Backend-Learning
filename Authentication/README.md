# Auth Lab API - Authentication Learning Journey

A comprehensive FastAPI laboratory for understanding authentication, authorization, and security concepts in backend development.

## 🎯 Learning Objectives

This project teaches you:
- **Authentication** - Verifying user identity ("Who are you?")
- **Authorization** - Controlling access ("What can you do?")
- **Sessions** - Stateful authentication with server-side storage
- **JWT** - Stateless authentication with self-contained tokens
- **API Keys** - Machine-to-machine authentication
- **RBAC** - Role-Based Access Control
- **Cookies** - Client-side session management
- **Security Tradeoffs** - Understanding when to use each approach

## 🚀 Features Implemented

### Session-Based Authentication
- `POST /login` - Login with username/password, receives session cookie
- `GET /profile` - Protected route requiring valid session
- `POST /logout` - Invalidate session and clear cookie
- `GET /admin` - Admin-only route using RBAC

### JWT Authentication
- `POST /jwt/login` - Login and receive JWT token
- `GET /jwt/profile` - Protected route using JWT
- `GET /jwt/admin` - Admin-only route using JWT claims

### API Key Authentication
- `POST /generate-api-key` - Generate API key for applications
- `GET /api/data` - Protected route requiring valid API key

## 📋 Prerequisites

- Python 3.8+
- pip

## 🛠️ Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd Authentication

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

Interactive API documentation: `http://localhost:8000/docs`

## 👥 Test Users

| Username | Password | Role |
|----------|----------|------|
| admin    | admin    | admin |
| user     | user     | user |
| moderator| moderator| moderator |

## 📚 Learning Path

### Task 1: Project Structure
Understanding how to organize a FastAPI project with routers, models, and auth modules.

### Task 2: User Store
Creating an in-memory user database with roles.

### Task 3: Login Endpoint
Implementing username/password authentication.

### Task 4: Session Management
Stateful authentication with server-side session storage.

### Task 5: Cookie Support
Automatically sending session IDs via HTTP cookies.

### Task 6: Protected Routes
Validating sessions before granting access.

### Task 7: Logout
Session revocation and cleanup.

### Task 8: JWT Authentication
Stateless authentication using JSON Web Tokens.

### Task 9: JWT Protected Routes
Validating JWT signatures and extracting claims.

### Task 10: Comparison
Understanding tradeoffs between sessions and JWT (see `COMPARISON.md`).

### Task 11: API Keys
Machine-to-machine authentication for applications.

### Task 12: Roles
Adding role information to user data.

### Task 13: RBAC
Implementing Role-Based Access Control.

### Task 14: JWT Claims
Authorization decisions using JWT claims without database lookup.

### Task 15: Token Revocation
Understanding the challenges of revoking stateless tokens.

### Task 16: Hybrid Approach
Using multiple authentication strategies in production.

## 🔐 Security Notes

⚠️ **This is a learning project. Do not use in production without modifications:**

- Passwords are stored in plain text (use bcrypt in production)
- Secret keys are hardcoded (use environment variables)
- No rate limiting
- No HTTPS enforcement
- In-memory storage (data lost on restart)

## 📖 Key Concepts

### Authentication vs Authorization
- **Authentication**: Verifying identity (login, tokens)
- **Authorization**: Checking permissions (roles, RBAC)

### Stateful vs Stateless
- **Stateful (Sessions)**: Server maintains user state, easy logout, harder to scale
- **Stateless (JWT)**: No server state, easy to scale, harder to revoke

### When to Use What
- **Sessions**: Browser apps, need immediate logout, simple deployment
- **JWT**: Mobile apps, APIs, microservices, cross-domain
- **API Keys**: Service-to-service communication, automated scripts

## 🛡️ Production Recommendations

For a production system:
1. Use bcrypt/argon2 for password hashing
2. Store secrets in environment variables
3. Add rate limiting
4. Implement refresh tokens for JWT
5. Use HTTPS everywhere
6. Add CSRF protection
7. Implement proper logging and monitoring
8. Use a real database (PostgreSQL, Redis)
9. Add input validation and sanitization
10. Implement proper error handling

## 📁 Project Structure

```
Authentication/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── COMPARISON.md          # Session vs JWT comparison
├── TASKS.md               # Task flow documentation
├── routers/               # API route handlers
│   ├── auth.py           # Session-based auth routes
│   ├── jwt_auth.py       # JWT auth routes
│   └── api_routes.py     # API key routes
├── auth/                  # Authentication logic
│   ├── session_manager.py # Session storage and management
│   ├── jwt_handler.py     # JWT creation and validation
│   └── api_key_manager.py # API key generation and validation
└── models/                # Data models
    └── user_store.py      # In-memory user database
```

## 🧪 Testing with Swagger UI

1. Start the server
2. Open `http://localhost:8000/docs`
3. Try the endpoints:
   - Login with session auth
   - Access protected routes
   - Try JWT authentication
   - Generate and use API keys
   - Test admin-only endpoints

## 🤝 Contributing

This is a learning project. Feel free to fork and experiment!

## 📝 License

MIT License - Feel free to use for learning purposes.

## 🎓 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [JWT.io](https://jwt.io/)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

---

**Happy Learning! 🚀**
