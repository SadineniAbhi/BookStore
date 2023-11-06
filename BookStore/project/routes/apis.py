from project import app, db
from flask import request,jsonify
from project.models import Book_model,OrderItem

@app.route('/api/books', methods=['GET',"POST","PUT"])
def get_all_books():
    
    response = {
        "error": {
            "code": 404,
            "message": "Error Retry Again!!",
        }
    }
    # Retrieve all books from your database
    books = Book_model.query.all()
    if request.method == "GET":
        books_list = []
        for book in books:
            books_list.append({
                'id': book.id,
                'title': book.title,
                'author': book.author,
                'isbn': book.isbn,
                'genre': book.genre,
                'price': book.price,
                'availability': book.availability,
            })
        
        return jsonify(books_list)

    if request.method == "POST":
        data = request.get_json()
        try:
            newbook = Book_model(data['title'],data['author'],data["isbn"],data["genre"],data['price'],data["availability"])
            db.session.add(newbook)
            db.session.commit()
            return jsonify({"message":"sucssesfully added the book"})
        except:
            return jsonify({"message":"Error while creating the new book"})
        
    if request.method == "PUT":
        data = request.get_json()
        try:
            reqiredbook = Book_model.query.get(data["id"])
            reqiredbook.availability = data["availability"]
            db.session.commit()
            return jsonify({"message":"succesfully update the availablity!"})
        except:
            return jsonify({"message":"Error while updating the book details"})
        
    return jsonify(response)


@app.route('/api/orders', methods=['GET',"PUT"])
def get_all_orders():
    response = {
        "error": {
            "code": 404,
            "message": "Error Retry Again!!",
        }
    }
    # Retrieve all books from your database
    
    if request.method == "GET":
        orders = OrderItem.query.all()

        # Serialize the books to a list of dictionaries
        orders_list = []
        for order in orders:
            orders_list.append({
                'id': order.id,
                'book_id': order.id,
                'orderstatus': order.orderstatus,
                'address': order.address,
                'bookname': order.book_name,
                'username': order.user_name,
            })
        # Return the serialized data as JSON
        return jsonify(orders_list)
        
    if request.method == "PUT":

        data = request.get_json()
        orderid = data["id"]
        requiredorder = OrderItem.query.get(orderid)

        if requiredorder:
            requiredorder.orderstatus = data['orderstatus']
            db.session.commit()
            return jsonify({"message":"succsfully updated the order"})
        else:
            return jsonify({"message":"No such order id exits"})
            
    return jsonify(response)