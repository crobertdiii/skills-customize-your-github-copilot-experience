from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API Starter")


class BookIn(BaseModel):
    title: str
    author: str
    year: int


books = {
    1: {"title": "1984", "author": "George Orwell", "year": 1949}
}


# Task 1: Return all books
@app.get("/books")
def get_books():
    pass


# Task 1: Return one book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


# Task 1: Create a new book
@app.post("/books", status_code=201)
def create_book(book: BookIn):
    pass


# Task 1: Update an existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookIn):
    pass


# Task 1: Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    pass


# Task 2:
# Run with: uvicorn starter-code:app --reload
# Then open: http://127.0.0.1:8000/docs
