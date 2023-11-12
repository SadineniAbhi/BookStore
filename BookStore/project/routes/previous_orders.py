from project import app
from flask import render_template
from project.services.get_previous_orders import get_previous_orders
from project import db
from flask_login import login_required,current_user


@app.route("/yourorders",methods=["GET"])
@login_required
def get_orders():
    booksordered = get_previous_orders()
    return render_template("previous_orders.html",book_details = booksordered)

