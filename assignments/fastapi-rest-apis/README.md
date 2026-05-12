# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice routing, request handling, and response design. By the end of this assignment, you will create and test API endpoints for a simple resource.

## 📝 Tasks

### 🛠️ Build Core CRUD Endpoints

#### Description
Create a FastAPI application that serves a simple in-memory collection of books. Implement endpoints to create, read, update, and delete book records.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by ID or a 404 response if missing.
- Implement `POST /books` to add a new book with `title`, `author`, and `year` fields.
- Implement `PUT /books/{book_id}` and `DELETE /books/{book_id}` for update and removal.

### 🛠️ Validate Input And Test Endpoints

#### Description
Add input validation and verify endpoint behavior using FastAPI's interactive docs.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data for create and update operations.
- Return clear success/error responses with appropriate HTTP status codes.
- Include at least one example book in the in-memory data store on startup.
- Run the app with Uvicorn and test all endpoints using `/docs`.
