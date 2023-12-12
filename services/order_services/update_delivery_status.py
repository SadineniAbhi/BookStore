from project.models.order_model import Order
def get_all_orders(id):
    books = Order.query.get(id)
    return books