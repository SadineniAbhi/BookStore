from project import db
from datetime import datetime
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=5)
    release_date = db.Column(db.DateTime, default=datetime.utcnow)  

    def __init__(self,isbn,title,author,genre,price,quantity,release_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity
        self.release_date = release_date
        self.isbn = isbn
