from project.models.book_model import Book
def getBookDetails(bookname):
    book = Book.query.filter_by(book_name=bookname).one_or_none()
    return book