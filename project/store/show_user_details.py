from project.models.user_model import User
from flask_jwt_extended import current_user

def getuserdetails():
    details = User.query.get(current_user.id)
    return details