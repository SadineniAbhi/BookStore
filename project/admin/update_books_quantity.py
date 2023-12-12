from flask_jwt_extended import jwt_required
from flask import request,jsonify
from project.admin import bp
from services.books_services.update_books_quantity import update_quantity
@bp.route("/update_quantity",methods=["POST"])
@jwt_required()
def update_books_quantity():
    book_name = request.json.get("book_name",None)
    quantity = request.json.get("quantity",None)
    try:
        update_quantity(book_name,quantity)
        return jsonify({'msg':'updated book quantity'})
    except:
        return jsonify({'msg':'unable to update bookquantity'})
    
