from project import db
import datetime
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(50),nullable = False, unique = True)
    author = db.Column(db.String(30),nullable = False)
    relase_date = db.Column(db.DateTime, nullable= False)
    price = db.Column(db.Integer,nullable = False)
    availability = db.Column(db.Integer,nullable = False)
    created_date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated_by = db.Column(db.Integer,db.ForeignKey('user.id'))
