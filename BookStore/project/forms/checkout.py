from flask_wtf import FlaskForm
from wtforms import SubmitField

class Checkout(FlaskForm):
    submit = SubmitField("Checkout")