from project import db
from project.models.book_model import Book
from project.services.buying_books.get_cart_items import get_cart_items
from flask_login import current_user

def get_books_in_cart():
    cart_items = get_cart_items()
    #stores book objects
    book_details = []
    for book in cart_items:
        book_details.append(Book.query.get(book.book_id))
    return book_details