from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length , EqualTo,Email, ValidationError
from project.models.user_model import User

#registration form
class Registration(FlaskForm):
    def validate_username(self,username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exits please try different username or login  ')
    def validate_email_address(self,email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email address already exits please try different username')

    username = StringField("User Name:",validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField("Email Address:",validators=[Email(),DataRequired()])
    address = StringField("Your Address:",validators=[DataRequired()])
    password1 = PasswordField("Password:",validators=[Length(min=6),DataRequired()])
    password2 = PasswordField("Confirm Password:",validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField("Create Account")
