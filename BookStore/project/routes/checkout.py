from project import app, db
from flask import flash,redirect,render_template,url_for
from project.forms.checkout import Checkout
from project.models.Book_model import Book
from project.models.cart_models import Cart
from project.models.order_models import Order, OrderItem
from flask_login import login_required, current_user

@app.route("/checkout",methods = ["GET","POST"])
@login_required
def checkout():
    form = Checkout()
    current = current_user
    if current.cart == None:
        newcart = Cart(user_id = current.id)
        db.session.add(newcart)
        db.session.commit()
    cart_items = current.cart.items.all()
    book_details = []
    for i in cart_items:
        book_details.append(Book.query.get(i.book_id))

    if form.validate_on_submit():
        if current.order == None:
            neworder = Order(user_id=current.id)
            db.session.add(neworder)
            db.session.commit()
        
        for j in book_details:
            if j.availability<=0:
                flash("few books are unavailabe ordering as many as possible",category="danger")
            else:
                j.availability-=1
                #this adds to the order table
                newitem = OrderItem(book_id = j.id, order_id = current.order.id,address = current.address,book_name = j.title,user_name = current.username)
                db.session.add(newitem)
                db.session.commit()
        for i in cart_items:
            db.session.delete(i)
        db.session.commit()
        return redirect(url_for("orders"))
    return render_template("checkout.html",book_details = book_details,form = form)