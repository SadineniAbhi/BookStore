from project import db

#each user has one orderid
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')
    

#each orderid has may books
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    orderstatus = db.Column(db.Text, default="Not Deliverd")
    address = db.Column(db.Text)
    book_name = db.Column(db.Text)
    user_name = db.Column(db.Text)