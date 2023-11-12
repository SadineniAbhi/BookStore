from project import db
from project.models.order_models import Order,OrderItem
from project.services.buying_books.get_books_in_cart import get_books_in_cart
from project.services.buying_books.get_cart_items import get_cart_items
from flask_login import current_user
from flask import flash

def buybooks():
    current = current_user
    books = get_books_in_cart()
    cart_items = get_cart_items()
    if current.order == None:
        neworder = Order(user_id=current.id)
        db.session.add(neworder)
        db.session.commit()
    
    for book in books:
        if book.availability<=0:
            flash("few books are unavailabe ordering as many as possible",category="danger")
        else:
            book.availability-=1
            #this adds to the order_items model
            boughtitem = OrderItem(book_id = book.id, order_id = current.order.id,address = current.address,book_name = book.title,user_name = current.username)
            db.session.add(boughtitem)
            db.session.commit()

    for book in cart_items:
        db.session.delete(book)

    db.session.commit()