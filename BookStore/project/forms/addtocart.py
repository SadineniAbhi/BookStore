from flask_wtf import FlaskForm
from wtforms import SubmitField

#forms for AddToCart button
class AddToCart(FlaskForm):
    submit = SubmitField("Add to Cart")