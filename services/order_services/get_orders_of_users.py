from project.models.order_model import Order
def get_all_orders():
    books = Order.query.all()
    return books