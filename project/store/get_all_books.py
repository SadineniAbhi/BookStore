from services.books_services.get_books import get_all_books
from project.store import bp 
from flask import jsonify

@bp.route("/getbooks",methods = ["GET"])
def getbooks():
    books = get_all_books()
    booksdict = {}


    for book in books:
        booksdict[book.id] = {
            'book_name' : book.book_name,
            'author' : book.author,
            'price' : book.price,
            'availability' : book.availability
        }
         
    return jsonify(booksdict)