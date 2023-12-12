from project.models.book_model import Book
def get_all_books():
    books = Book.query.all()
    return books