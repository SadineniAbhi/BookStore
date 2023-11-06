from project import app
from flask import render_template
from project.models.Book_model import Book
from project.models.order_models import Order
from project import db
from flask_login import login_required,current_user


@app.route("/yourorders")
@login_required
def orders():
    current = current_user
    if current.order == None:
        neworder = Order(user_id=current.id)
        db.session.add(neworder)
        db.session.commit()
    userorders = current.order.items.all()
    book_details = []
    for i in userorders:
        book_details.append(Book.query.get(i.book_id))
    return render_template("orders.html",book_details = book_details)
