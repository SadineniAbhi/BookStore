from project.models.book_model import Book
from project import app,db
def update_quantity(bookname,new_quantity):
    with app.app_context():
        book = Book.query.filter(Book.book_name==bookname).first()
        book.availability = new_quantity
        db.session.add(book)
        db.session.commit()