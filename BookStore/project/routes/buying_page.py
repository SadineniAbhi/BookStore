from project import app
from flask import redirect,render_template,url_for
from project.forms.checkout import Checkout
from flask_login import login_required
from project.services.buying_books.get_books_in_cart import get_books_in_cart
from project.services.buying_books.buybooks import buybooks

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
    if form.validate_on_submit():
        buybooks()
        return redirect(url_for('get_orders'))
    return render_template("buying_page.html",form = form)