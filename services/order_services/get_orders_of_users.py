from project.models.order_model import Order
def get_all_orders():
    orders = Order.query.all()
    return orders