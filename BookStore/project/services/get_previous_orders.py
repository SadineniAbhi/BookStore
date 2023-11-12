from flask_login import current_user
from project.models.order_models import Order
from project.models.book_model import Book
from project import db
def get_previous_orders():
    current = current_user
    if current.order == None:
        neworder = Order(user_id=current.id)
        db.session.add(neworder)
        db.session.commit()
    userorders = current.order.items.all()
    book_details = []
    for book in userorders:
        book_details.append(Book.query.get(book.book_id))
    return book_details