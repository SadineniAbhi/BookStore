from project.models.book_model import Book

def get_books():
    books = Book.query.all()
    return books