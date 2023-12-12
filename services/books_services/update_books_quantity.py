from project.models.book_model import Book
from project import db
from flask_jwt_extended import current_user
import datetime
def update_quantity(bookname,new_quantity):
    book = Book.query.filter(Book.book_name==bookname).first()
    book.availability = book.availability + new_quantity
    book.last_updated = datetime.datetime.now()
    book.last_updated_by = current_user.id
    db.session.add(book)
    db.session.commit()