from project import app,db
from flask import render_template,redirect,url_for,request
from project.models.Book_model import Book
from project.models.cart_models import Cart, CartItem
from project.forms.addtocart import AddToCart
from flask_login import current_user

@app.route("/store", methods = ["GET","POST"])
def store():
    current = current_user
    books = Book.query.all()
    form = AddToCart()
    if form.validate_on_submit():
        book_id = int(request.form['book_id'])
        if book_id:
            if current.cart == None:
                newcart = Cart(user_id = current.id)
                db.session.add(newcart)
                db.session.commit()
            cart_item = CartItem(cart_id=current.cart.id, book_id=book_id)
            db.session.add(cart_item)
            db.session.commit()
        return redirect(url_for("checkout"))
    return render_template("store.html",books = books,form = form)