# Backend Introduction — Notes + Implementation

## What is Backend?

Backend is the part of an application that runs on a **server** and handles:

- Receiving requests from clients (browser, mobile apps, other services)
- Executing business logic
- Communicating with databases
- Interacting with external services
- Sending responses back to clients

Common protocols used by backend systems:

- HTTP
- WebSocket
- gRPC

Backend services run on specific **ports** like:

```
3000
5000
8000
8080
```

---

# How Backend Works (Production Flow)

Typical request flow in real systems:

```
Client (Browser / Mobile App)
        ↓
DNS Resolution
        ↓
Load Balancer
        ↓
Web Server (Nginx / Apache)
        ↓
Backend Application (Django / Node / Java / Go)
        ↓
Database / External Services
        ↓
Response back to Client
```

---

# Why Backend is Required

Backend is necessary for:

- Security
- Authentication & Authorization
- Business logic execution
- Data validation
- Database management
- API management
- Performance & scalability
- Centralized data control

Example:

When you like a post on Instagram:

Backend will:
1. Identify the user
2. Validate the request
3. Store the like in database
4. Update like count
5. Notify the post owner
6. Send response

---

# Why Frontend Should NOT Access Database Directly

Direct frontend-to-database access causes:

- Security risks
- Exposed credentials
- No validation
- No access control
- Data corruption risks
- No monitoring or logging
- No scalability control

Backend acts as a **secure gatekeeper**.

---

# Difference Between Web Server and Backend Application

## Web Server (Nginx / Apache)

Responsible for:

- Handling incoming internet traffic
- Serving static files (HTML, CSS, JS)
- Reverse proxy to backend
- Load management
- Security filtering

Think of it as a **traffic controller**.

## Backend Application (Django)

Responsible for:

- Business logic
- API creation
- Authentication
- Validation
- Database operations

Think of it as the **brain of the system**.

---

# Django Backend Request Flow

In Django:

```
Client
   ↓
urls.py
   ↓
views.py
   ↓
models.py (database)
   ↓
Response (JSON / HTML)
```

Important components:

```
urls.py → Route requests
views.py → Business logic
models.py → Database layer
serializers → Validation & transformation
```

---

# Installing Django and Django REST Framework

```
pip install django djangorestframework
```

---

# Create Django Project

```
django-admin startproject production_backend
```

---

# Navigate into Project

```
cd production_backend
```

---

# Run Development Server

```
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

# Creating an App (Production Practice)

In production backends, features are divided into **apps (modules)**.

```
python manage.py startapp core
```

---

# Register App in settings.py

Whenever a new app is created, it must be registered.

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "core",
]
```

---

# First Backend API — Health Check Endpoint

Production systems always have a health endpoint used by:

- Load balancers
- Monitoring tools
- DevOps systems
- Kubernetes
- Auto-scaling systems

Endpoint:

```
GET /api/health/
```

---

# Implementation

## core/views.py

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def healthcheck(request):
    return Response({
        "status": "running",
        "service": "production_backend",
        "message": "Backend is working correctly"
    })
```

---

## core/urls.py

```python
from django.urls import path
from .views import healthcheck

urlpatterns = [
    path("health/", healthcheck),
]
```

---

## project urls.py

File:
```
production_backend/urls.py
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
]
```

Final endpoint:

```
http://127.0.0.1:8000/api/health/
```

---

# Important Backend Interview Concepts

## Why Health Endpoints Exist

Used for:

- Server monitoring
- Load balancer health checks
- Auto scaling
- System reliability

Example:

```
/health
```

---

# Public vs Internal Health Checks

Public:

```
/health
```

Internal monitoring:

```
/internal/health
```

Internal endpoints may require authentication.

---

# Backend System Design Example — Like a Post

When a user likes a post:

```
Client
 → Load Balancer
 → Web Server (Nginx)
 → Backend (Django)
 → Business Logic
 → Database Update
 → Notification System
 → Response
```

---

# Concurrency Problem in Backend Systems

When multiple users perform actions at the same time, issues can occur.

Example:

Two users liking a post simultaneously.

Problem:

```
Race Condition
```

Example issue:

```
Current Likes = 100

Server A reads = 100
Server B reads = 100

Server A writes = 101
Server B writes = 101
```

Final value becomes incorrect.

---

# Production Solution

Use **Atomic Database Updates**

Example concept:

```
UPDATE posts SET likes = likes + 1
```

In Django (later topic):

```
F expressions
```

---

# Key Backend Concepts Learned in Topic 01

You now understand:

- What backend is
- How production backend systems work
- Difference between web server and backend
- Django request flow
- API routing
- Building a health endpoint
- Backend architecture basics
- Concurrency problems
- Race conditions
- Production system thinking