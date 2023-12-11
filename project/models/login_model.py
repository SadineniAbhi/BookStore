import datetime
from project.extensions import db 
from project.models.user_model import User
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_time = db.Column(db.DateTime,nullable = False)
    logout_time = db.Column(db.DateTime,nullable = False)
    created_date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated_by = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    