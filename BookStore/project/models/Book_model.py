from project import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    genre = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Integer, default=True)

    def __init__(self,title,author,isbn,genre,price,availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.availability = availability