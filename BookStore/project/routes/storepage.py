from project import app
from flask import render_template,redirect,url_for,request
from project.forms.addtocart import AddToCart
from project.services.get_books import get_books
from project.services.add_to_cart_model import add_to_cart_model

@app.route('/')
@app.route("/store",methods =["GET"])
def show_books():
    form = AddToCart()
    books = get_books()
    return render_template("store_page.html",books = books,form = form)

@app.route("/store", methods = ["POST"])
def add_to_cart():

    form = AddToCart()
    if form.validate_on_submit():
        book_id = int(request.form['book_id'])
        if book_id:
            add_to_cart_model(book_id)
        return redirect(url_for("get_cart_items"))
    return render_template("store_page.html",form = form)




