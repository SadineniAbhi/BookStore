from project.models.book_model import Book
from project import db
def del_book(bookname):
    book = Book.query.filter(Book.book_name==bookname).first()
    db.session.delete(book)
    db.session.commit()