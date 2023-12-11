from project.extensions import db
from project.models.book_model import Book
from project.models.user_model import User
import datetime
class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    quantity = db.Column(db.Integer,nullable=False,default = 1)
    status_code = db.Column(db.Integer,db.ForeignKey('delivery.status_code'),nullable = False)
    created_date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated_by = db.Column(db.Integer,db.ForeignKey('user.id'))

#look up table 
class Delivery(db.Model):
    status_code = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(15),nullable = True,unique = True)