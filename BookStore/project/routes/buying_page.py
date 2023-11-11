from project import app, db
from flask import flash,redirect,render_template,url_for
from project.forms.checkout import Checkout
from project.models.Book_model import Book
from project.models.order_models import Order, OrderItem
from flask_login import login_required, current_user
from project.services.get_books_in_cart import get_books_in_cart

@app.route("/checkout",methods = ["GET"])
@login_required
def get_cart_items():
    form = Checkout()
    books_in_cart = get_books_in_cart()
    return render_template("buying_page.html",book_details=books_in_cart,form=form)

@app.route("/checkout",methods = ["POST"])
@login_required
def place_order():
    form = Checkout()
    current = current_user

    cart_items = current.cart.items.all()
    books = []
    for book in cart_items:
        books.append(Book.query.get(book.book_id))

    if form.validate_on_submit():
        if current.order == None:
            neworder = Order(user_id=current.id)
            db.session.add(neworder)
            db.session.commit()
        
        for book in books:
            if book.availability<=0:
                flash("few books are unavailabe ordering as many as possible",category="danger")
            else:
                book.availability-=1
                #this adds to the order_items model
                boughtitem = OrderItem(book_id = book.id, order_id = current.order.id,address = current.address,book_name = book.title,user_name = current.username)
                db.session.add(boughtitem)
                db.session.commit()

        for book in cart_items:
            db.session.delete(book)

        db.session.commit()
        return redirect(url_for("get_orders"))
    return render_template("buying_page.html",form = form)