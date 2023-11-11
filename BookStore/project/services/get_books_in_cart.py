from project import db
from project.forms.checkout import Checkout
from project.models.Book_model import Book
from project.models.cart_models import Cart
from project.models.order_models import Order, OrderItem
from flask_login import login_required, current_user

def get_books_in_cart():
    current = current_user
    if current.cart == None:
        newcart = Cart(user_id = current.id)
        db.session.add(newcart)
        db.session.commit()
        #get cart objects
    cart_items = current.cart.items.all()
    #stores book objects
    book_details = []
    for book in cart_items:
        book_details.append(Book.query.get(book.book_id))
    return book_details