from project.admin import bp 
from flask import json,request,jsonify
from services.books_services.add_book import addbooks
from flask_jwt_extended import jwt_required,current_user

@bp.route("/addbooks",methods = ["GET","POST"])
@jwt_required()
def add_books():
    if not current_user.is_admin:
        return jsonify({"msg":"unAuthorized"})
    book_name = request.json.get('book_name')
    author = request.json.get("author")
    price = request.json.get("price")
    availability = request.json.get("availability")
    addbooks(book_name=book_name,author=author,price=price,availability=availability,last_updated_by = current_user.id)
    try:
        return jsonify({"msg":'added books!'}),200
    except:
        return jsonify({'msg':'can not add books!'}),500
    

