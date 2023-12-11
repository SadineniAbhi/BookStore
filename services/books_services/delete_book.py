from project.models.book_model import Book
from project import app,db
def update_quantity(bookname):
    with app.app_context():
        book = Book.query.filter(Book.book_name==bookname).first()
        db.session.delete(book)
        db.session.commit()