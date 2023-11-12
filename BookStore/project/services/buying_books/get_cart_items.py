from flask_login import current_user
from project.models.cart_models import Cart
from project import db
def get_cart_items():
     if current_user.cart == None:
        newcart = Cart(user_id = current_user.id)
        db.session.add(newcart)
        db.session.commit()
     cart_items = current_user.cart.items.all()
     return cart_items