# HTTP Protocol & Backend Fundamentals

---

# 1. Why Learn HTTP?

Backend systems are huge, but **90% of applications communicate through HTTP**.

Whenever:

- Browser talks to server
- Mobile app talks to API
- Frontend fetches data
- Client uploads files

HTTP is usually involved.

---

# 2. Core Ideas Behind HTTP

## 2.1 Statelessness

### What is Stateless?

HTTP does **not remember previous requests**.

Every request is treated independently.

Example:

```
Request 1:
GET /profile

Request 2:
GET /orders
```

The server treats Request 2 as a completely new request.

It doesn’t automatically remember Request 1.

---

### Why?

Each request contains everything needed:

- URL
- Headers
- Cookies
- Tokens
- Body

Server processes it and forgets it.

---

### Example

User opens profile page.

Request:

```
GET /profile
Authorization: Bearer xyz
```

Server checks token.

Response sent.

Memory forgotten.

Next request must send token again.

---

### Benefits

### 1. Simplicity

No need to store user session information in memory.

---

### 2. Scalability

Request can go to any server.

```
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
```

Works perfectly.

---

### 3. Fault Tolerance

If one server crashes:

```
Server A ❌
```

Next request can go to:

```
Server B ✅
```

No session state lost.

---

### Problem with Statelessness

Applications need continuity.

Examples:

- Login
- Shopping cart
- User preferences

Solutions:

- Cookies
- Sessions
- JWT Tokens

---

# 3. Client-Server Model

HTTP follows a Client-Server architecture.

---

## Client

Initiates request.

Examples:

- Browser
- Mobile App
- Postman
- Frontend Application

---

## Server

Responds to requests.

Examples:

- Node.js API
- Django Server
- Spring Boot Application

---

Flow:

```
Client
   |
   | Request
   v
Server
   |
   | Response
   v
Client
```

Important:

### Client always initiates communication.

Server never starts HTTP communication.

---

# 4. HTTP vs HTTPS

### HTTP

Data sent as plain text.

---

### HTTPS

HTTP + Security

Provides:

- Encryption
- TLS
- Certificates

Benefits:

- Secure communication
- Prevents interception
- Prevents tampering

---

# 5. HTTP Uses TCP

HTTP needs reliable communication.

Two common transport protocols:

## TCP

Reliable

Features:

- Ordered delivery
- Error detection
- Connection based

HTTP traditionally uses TCP.

---

## UDP

Fast but unreliable.

No guarantee of delivery.

---

# 6. OSI Model (Backend Perspective)

```
7 Application Layer  ← HTTP
6 Presentation
5 Session
4 Transport Layer    ← TCP/UDP
3 Network
2 Data Link
1 Physical
```

Backend developers mostly work with:

### Layer 7

Application Layer

Examples:

- HTTP
- REST APIs
- GraphQL

---

# 7. Evolution of HTTP

---

## HTTP 1.0

Each request:

```
Open Connection
Send Request
Receive Response
Close Connection
```

Very slow.

---

## HTTP 1.1

Introduced:

### Persistent Connections

Reuse same TCP connection.

Benefits:

- Faster
- Less overhead

Also introduced:

- Better caching
- Chunked transfer

---

## HTTP 2

Introduced:

### Multiplexing

Multiple requests simultaneously over one connection.

Benefits:

- Faster loading
- Reduced latency

---

## HTTP 3

Built on:

```
QUIC + UDP
```

Benefits:

- Faster connection setup
- Better packet loss handling
- Lower latency

---

# 8. Structure of HTTP Message

---

## Request

```
GET /users HTTP/1.1

Host: api.com
Authorization: Bearer xyz

Body
```

Contains:

1. Method
2. URL
3. Version
4. Headers
5. Body

---

## Response

```
HTTP/1.1 200 OK

Content-Type: application/json

{
  "name":"Abhi"
}
```

Contains:

1. Version
2. Status Code
3. Headers
4. Body

---

# 9. HTTP Headers

Headers are:

```
Key → Value
```

metadata about request/response.

Example:

```
Content-Type: application/json
```

---

## Why Headers Exist?

Think of a courier package.

Package contains actual item.

Label contains:

- Address
- Phone number
- Sender

Headers are the label.

Body is the actual package.

---

# 10. Types of Headers

---

## Request Headers

Sent by client.

Examples:

```
Authorization
User-Agent
Accept
```

Purpose:

Describe request.

---

## General Headers

Used by both request and response.

Examples:

```
Date
Cache-Control
Connection
```

---

## Representation Headers

Describe body.

Examples:

```
Content-Type
Content-Length
Content-Encoding
ETag
```

---

## Security Headers

Examples:

```
Strict-Transport-Security
Content-Security-Policy
X-Frame-Options
Set-Cookie
```

Purpose:

Protect against:

- XSS
- Clickjacking
- MIME sniffing

---

# 11. Two Powerful Ideas of Headers

---

## Extensibility

New headers can be added without changing HTTP.

Example:

```
X-Custom-Header
```

---

## Remote Control

Headers influence server behavior.

Example:

```
Accept: application/json
```

Server responds with JSON.

---

# 12. HTTP Methods

Methods describe the intention of request.

---

## GET

Fetch data.

```
GET /users
```

Should NOT modify data.

---

## POST

Create data.

```
POST /users
```

Contains body.

---

## PATCH

Partial update.

```
PATCH /profile
```

Example:

```json
{
  "name":"Abhi"
}
```

Updates only name.

---

## PUT

Complete replacement.

Old resource:

```json
{
 "name":"Abhi",
 "age":20
}
```

PUT:

```json
{
 "name":"John"
}
```

Entire resource replaced.

---

## DELETE

Remove resource.

```
DELETE /users/5
```

---

# 13. Idempotency

## Meaning

Repeated requests produce same result.

---

## Idempotent Methods

### GET

```
GET /users
GET /users
GET /users
```

Same result.

---

### PUT

Replacing same data repeatedly.

Same outcome.

---

### DELETE

Delete once.

Repeated deletes don’t change state.

---

## Non-Idempotent

### POST

```
POST /notes
```

Creates new note every time.

Different result.

Not idempotent.

---

# 14. CORS (Cross-Origin Resource Sharing)

---

## Same Origin Policy

Browser blocks requests between different origins.

Example:

```
Frontend:
example.com

Backend:
api.example.com
```

Different origin.

Blocked unless CORS allows.

---

# 15. Simple Request Flow

Browser sends:

```
Origin: example.com
```

Server responds:

```
Access-Control-Allow-Origin: example.com
```

or

```
Access-Control-Allow-Origin: *
```

Browser allows response.

Otherwise:

```
CORS Error
```

---

# 16. Preflight Request

Triggered when:

### Condition 1

Method is:

```
PUT
DELETE
```

---

### Condition 2

Custom headers exist.

Example:

```
Authorization
```

---

### Condition 3

Content-Type:

```
application/json
```

---

## Browser Sends OPTIONS Request

```
OPTIONS /users
```

Purpose:

Ask server permissions.

---

Server responds:

```
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
```

Browser verifies.

Then sends actual request.

---

# 17. HTTP Status Codes

Purpose:

Standardized communication.

---

## 1xx Informational

### 100 Continue

Proceed with request body.

---

### 101 Switching Protocols

Example:

```
HTTP → WebSocket
```

---

# 18. Success Codes (2xx)

---

## 200 OK

Request successful.

---

## 201 Created

New resource created.

Usually POST.

---

## 204 No Content

Success but no body returned.

Common:

- DELETE
- OPTIONS

---

# 19. Redirection (3xx)

---

## 301 Moved Permanently

Permanent redirect.

---

## 302 Found

Temporary redirect.

---

## 304 Not Modified

Used for caching.

Server says:

```
Use cached version.
```

---

# 20. Client Errors (4xx)

---

## 400 Bad Request

Invalid data.

---

## 401 Unauthorized

Missing/invalid authentication.

---

## 403 Forbidden

Authenticated but lacks permission.

---

## 404 Not Found

Resource doesn’t exist.

---

## 405 Method Not Allowed

Wrong HTTP method.

---

## 409 Conflict

Resource already exists.

---

## 429 Too Many Requests

Rate limit exceeded.

---

# 21. Server Errors (5xx)

---

## 500 Internal Server Error

Unexpected server failure.

---

## 501 Not Implemented

Feature unsupported.

---

## 502 Bad Gateway

Proxy got invalid response.

---

## 503 Service Unavailable

Server temporarily unavailable.

---

## 504 Gateway Timeout

Proxy waited too long.

---

# 22. HTTP Caching

Goal:

Avoid unnecessary server requests.

Benefits:

- Faster loading
- Reduced bandwidth
- Reduced server load

---

## Important Headers

### Cache-Control

```
Cache-Control: max-age=10
```

Cache for 10 seconds.

---

### ETag

Unique resource identifier.

Usually hash.

Example:

```
ETag: "3141"
```

---

### Last-Modified

```
Last-Modified: Tue, 10 Jun
```

---

# Cache Flow

Browser sends:

```
If-None-Match: "3141"
```

Server checks.

If unchanged:

```
304 Not Modified
```

Browser uses cached copy.

No data transfer.

---

# 23. Content Negotiation

Client and server agree on format.

---

## Media Type Negotiation

```
Accept: application/json
```

or

```
Accept: application/xml
```

---

## Language Negotiation

```
Accept-Language: en
```

or

```
Accept-Language: es
```

---

## Encoding Negotiation

```
Accept-Encoding: gzip
```

---

# 24. HTTP Compression

Problem:

Large response.

Example:

```
26 MB JSON
```

Very expensive.

---

Solution:

```
Content-Encoding: gzip
```

Compressed response.

Example:

```
26 MB → 3.8 MB
```

Huge bandwidth savings.

---

# 25. Persistent Connections (Keep-Alive)

Before HTTP 1.1:

```
Open TCP
Request
Response
Close TCP
```

For every request.

Slow.

---

HTTP 1.1:

```
Open TCP once
Request 1
Request 2
Request 3
Close later
```

Benefits:

- Lower latency
- Less CPU
- Better performance

---

# 26. Multipart Form Data

Used for:

- Images
- Videos
- PDFs
- Audio files

Example:

```
Content-Type:
multipart/form-data
```

File transferred in parts.

Uses:

```
boundary=xyz123
```

Boundary separates chunks.

---

# 27. Chunked Transfer / Streaming

Used when server sends huge data.

Instead of:

```
Wait for full file
```

Server sends:

```
Chunk 1
Chunk 2
Chunk 3
...
```

Benefits:

- Faster perceived performance
- Lower memory usage

Headers:

```
Content-Type: text/event-stream
Connection: keep-alive
```

---

# Interview Revision Sheet (Must Memorize)

### Stateless

Server remembers nothing.

---

### Most Important Headers

```
Authorization
Content-Type
Accept
Cache-Control
ETag
```

---

### Most Important Methods

```
GET
POST
PATCH
PUT
DELETE
OPTIONS
```

---

### Most Important Status Codes

```
200 OK
201 Created
204 No Content
301 Moved
304 Not Modified
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
429 Too Many Requests
500 Internal Server Error
503 Service Unavailable
```

---

### Most Important Concepts

1. Statelessness
2. Client-Server Model
3. HTTP Headers
4. HTTP Methods
5. Idempotency
6. CORS
7. Status Codes
8. Caching
9. Content Negotiation
10. Compression
11. Keep-Alive
12. Multipart Uploads
13. Chunked Transfer

These are the HTTP topics that cover **the majority of backend interview questions and day-to-day backend development work**.