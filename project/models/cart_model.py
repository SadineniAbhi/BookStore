from project import db
from project.models.book_model import Book
from project.models.user_model import User
import datetime
class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer,db.ForeignKey('book.id'),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    quantity = db.Column(db.Integer,nullable=False,default = 1)
    saved_for_later = db.Column(db.Boolean, default = False)
    created_date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated_by = db.Column(db.Integer,db.ForeignKey('user.id'))

