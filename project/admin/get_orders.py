from services.order_services.get_orders_of_users import get_all_orders
from project.store import bp 
from flask import jsonify
from services.books_services.get_book_details import getBookDetails
from flask_jwt_extended import jwt_required,current_user

@bp.route("/getorders",methods = ["GET"])
@jwt_required()
def getorders():
    if not current_user.is_admin:
        return jsonify({"msg":"unAuthorized"})
    
    orders = get_all_orders()
    ordersdict = {}


    for order in orders:
        order[order.id] = {
            'book_id' : order.book_id,
            'book_name': getBookDetails(order.book_id).book_name,
            'quantity' : order.quantity,
            'status_code' : order.status_code
        }
         
    return jsonify(ordersdict)