from project.models.book_model import Book
from project import app
def get_all_books():
    with app.app_context():
        books = Book.query.all()
    return books