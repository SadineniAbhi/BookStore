from project import db 
from project.models.book_model import Book
def addbooks(book_name,author,price,availability,last_updated_by):
    newbook = Book(book_name=book_name,
                   author = author,price = price,
                   availability = availability,
                   last_updated_by=last_updated_by)
    db.session.add(newbook)
    db.session.commit()
    
