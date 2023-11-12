from project import db

from project.models.cart_models import Cart,CartItem
from flask_login import current_user


def add_to_cart_model(book_id):
    current = current_user
    if current.cart == None:
        newcart = Cart(user_id = current.id)
        db.session.add(newcart)
        db.session.commit()
    cart_item = CartItem(cart_id=current.cart.id, book_id=book_id)
    db.session.add(cart_item)
    db.session.commit()