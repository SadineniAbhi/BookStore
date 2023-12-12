from project.admin import bp 
from flask_jwt_extended import jwt_required
from flask import request,jsonify
from services.books_services.delete_book import del_book
@bp.route("/delete_book",methods = ["POST","GET"])
@jwt_required()
def delete_books():
    book_name = request.json.get("book_name",None)
    try:
        del_book(book_name)
        return jsonify({'msg':"deleted book"})
    except:
        return jsonify({'msg':"error not able to delete"})
    
