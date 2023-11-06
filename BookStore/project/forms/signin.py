from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired


class Signin(FlaskForm):    
    username = StringField("User Name:",validators=[DataRequired()])
    password = PasswordField("Password:",validators=[DataRequired()])
    submit = SubmitField("Sign in!")