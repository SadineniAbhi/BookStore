from project.models.user_model import User
from project.extensions import db
def add_user(username,email,password,last_updated_by):
    new_user = User(username = username,email = email,password = password,last_updated_by = last_updated_by)
    db.session.add(new_user)
    db.session.commit()