# HTTP Fundamentals for Backend Engineers

This document explains how HTTP works from a **backend engineering perspective** and how it is used when building APIs using **Django and Django REST Framework (DRF)**.

---

# What is HTTP?

HTTP (HyperText Transfer Protocol) is the communication protocol used between:

Client → Server

Examples of clients:
- Browser
- Mobile app
- Postman
- Another backend service

The backend receives HTTP requests and sends HTTP responses.

---

# Two Core Ideas of HTTP

HTTP is built on:

1. Stateless Model
2. Client–Server Model

---

# Stateless Model

HTTP is **stateless**.

This means:

The server does NOT remember previous requests.

Every request must contain all necessary information.

Example:

Request must include:
- Headers
- Method
- URL
- Body (optional)

Example request:

```
POST /login
Authorization: Bearer token
Content-Type: application/json
```

Server processes → sends response → forgets the request.

---

# Why Stateless Systems are Powerful

### 1 Simplicity
Server does not need to manage session memory.

### 2 Scalability
Requests can go to **any server** behind a load balancer.

Example:

User request → Load balancer → Server A  
Next request → Load balancer → Server B

Both work.

### 3 Reliability
If a server crashes, another server can handle the request.

---

# How State is Maintained in Real Systems

Even though HTTP is stateless, applications maintain state using:

Cookies  
Sessions  
JWT Tokens  
OAuth Tokens

Example login flow:

```
User logs in
Server creates session
Session ID stored in cookie
Next request sends cookie
Server identifies user
```

---

# Client–Server Model

HTTP follows client-server architecture.

Client responsibilities:
- Send request
- Provide data
- Call API

Server responsibilities:
- Process request
- Run business logic
- Access database
- Send response

Important rule:

Client always initiates communication.

---

# HTTP vs HTTPS

HTTP → Data sent as plain text  
HTTPS → Data encrypted using TLS/SSL

Production systems MUST use HTTPS.

Reasons:
- Security
- Prevent data interception
- Authentication
- Data integrity

---

# Transport Layer

HTTP runs on top of:

TCP (Transmission Control Protocol)

TCP provides:
- Reliable delivery
- Ordered packets
- Error correction

---

# TCP vs UDP

TCP
Reliable
Slower
Used by HTTP/1.1 and HTTP/2

UDP
Faster
No guarantee of delivery

HTTP/3 uses:
QUIC protocol over UDP

---

# OSI Model (Important for Backend Engineers)

7 Layers:

1 Physical  
2 Data Link  
3 Network  
4 Transport  
5 Session  
6 Presentation  
7 Application

Backend engineers mostly work at:

Layer 7 → Application Layer

This includes:
- APIs
- Authentication
- JSON responses
- Business logic

---

# Evolution of HTTP

### HTTP/0.9
Only GET requests.

### HTTP/1.0
Introduced:
Headers
Status codes

Problem:
New TCP connection for every request.

---

### HTTP/1.1
Major improvement.

Introduced:
Persistent connections

Problem:
Head-of-line blocking.

---

### HTTP/2
Multiplexing
Binary protocol
Header compression

Faster performance.

---

### HTTP/3
Uses QUIC over UDP.

Advantages:
No TCP head-of-line blocking.

Better for mobile networks.

---

# HTTP Message Structure

Two types:

HTTP Request  
HTTP Response

---

# HTTP Request

Structure:

Method  
URL  
Version  
Headers  
Body (optional)

Example:

```
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Bearer token

{
  "email": "user@email.com",
  "password": "123456"
}
```

---

# HTTP Response

Structure:

Version  
Status Code  
Headers  
Body

Example:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "success": true
}
```

---

# Why Headers Exist

Headers store **metadata**.

They tell the server how to process the request.

Example:

Authorization
Content-Type
Cache-Control
User-Agent

Headers are important because:

- Security
- Caching
- Authentication
- Content negotiation

---

# Types of Headers

### Request Headers
Sent by client.

Examples:
Authorization
User-Agent
Cookie
Accept

---

### General Headers

Examples:
Date
Connection
Cache-Control

---

### Representation Headers

Describe response body.

Examples:
Content-Type
Content-Length
ETag

---

### Security Headers

Examples:
HSTS
CSP
X-Frame-Options
Set-Cookie

---

# HTTP Methods

Methods define actions on resources.

GET → Fetch data  
POST → Create data  
PUT → Replace resource  
PATCH → Partial update  
DELETE → Remove resource

---

# Idempotent Methods

Idempotent means:
Repeating the request gives same result.

Idempotent methods:

GET  
PUT  
DELETE

Not idempotent:

POST  
PATCH

---

# Example Requests

GET

```
GET /users/1
```

POST

```
POST /users
```

PATCH

```
PATCH /users/1
```

DELETE

```
DELETE /users/1
```

---

# CORS and OPTIONS Method

CORS = Cross Origin Resource Sharing

Used when:

Frontend and backend are on different domains.

Example:

Frontend
example.com

Backend
api.example.com

Browser sends:

Preflight request (OPTIONS)

```
OPTIONS /api/users
```

Server responds:

Allowed methods  
Allowed headers

Then actual request happens.

---

# HTTP Status Codes

Status codes explain the result of a request.

Categories:

1xx Information  
2xx Success  
3xx Redirection  
4xx Client Error  
5xx Server Error

---

# Important Status Codes

200 OK → Success  
201 Created → Resource created  
204 No Content → Success without response body  

400 Bad Request → Invalid input  
401 Unauthorized → Login required  
403 Forbidden → Permission denied  
404 Not Found → Resource missing  
405 Method Not Allowed → Wrong method  

409 Conflict → Duplicate resource  
429 Too Many Requests → Rate limit

500 Internal Server Error → Server crashed  
503 Service Unavailable → Server overloaded

---

# HTTP Caching

Caching improves performance.

Benefits:
- Faster responses
- Reduced server load
- Reduced bandwidth

Important headers:

Cache-Control  
ETag  
Last-Modified

Example:

If resource not changed:

Server returns

304 Not Modified

---

# Content Negotiation

Client and server decide:

Response format.

Example:

JSON  
XML

Header used:

Accept

---

# Compression

Used to reduce response size.

Example:

gzip  
deflate

Reduces bandwidth usage.

---

# Django + DRF Implementation

Example API:

```
core/views.py
```

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "POST"])
def http_demo(request):

    if request.method == "GET":
        return Response({
            "method": "GET",
            "message": "Fetching data from server"
        })

    if request.method == "POST":
        return Response({
            "method": "POST",
            "message": "Data received",
            "data": request.data
        })
```

---

# Register Route

```
core/urls.py
```

```python
from django.urls import path
from .views import http_demo

urlpatterns = [
    path("http-demo/", http_demo)
]
```

---

# Connect to Project

```
project/urls.py
```

```python
from django.urls import path, include

urlpatterns = [
    path("api/", include("core.urls")),
]
```

---

# Test Using Postman

GET

```
http://127.0.0.1:8000/api/http-demo/
```

POST

```
http://127.0.0.1:8000/api/http-demo/
```

Body:

```
{
  "name": "Yadnyesh"
}
```

---

# Backend Engineering Best Practices

Never use GET for:

Payments  
Updating data  
Deleting data

Use correct methods.

Follow REST standards.

---

# Interview Questions

### Basic Level

What is HTTP?  
Why is HTTP stateless?  
Difference between HTTP and HTTPS?  
What is an HTTP request?

---

### Intermediate Level

Explain PUT vs PATCH.  
What are idempotent methods?  
Why are headers important?  
Explain status code categories.

---

### Advanced Level

Explain CORS flow.  
What is preflight request?  
Why POST should not be cached?  
How load balancers help stateless systems?

---

# Real Interview Questions (Amazon / Stripe / Uber)

Why should GET never modify data?  

What happens if a payment API uses GET?

Design an API for updating user profile.

Explain how browsers enforce CORS.

Why status codes are important in distributed systems?

---

# Summary

HTTP is the backbone of backend systems.

Understanding:

Requests  
Responses  
Methods  
Headers  
Status codes  
Caching  
CORS

is essential for building production-grade APIs.
