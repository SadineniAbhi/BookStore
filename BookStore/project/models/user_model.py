from project import db,login_manager,bcrypt,app
from flask_login import UserMixin



#loads the current user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#table for users
class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    address = db.Column(db.String(),nullable = False)
    isadmin = db.Column(db.Boolean(),default = False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    cart = db.relationship('Cart', backref='user', lazy=True, uselist = False)
    order = db.relationship('Order', backref='user', lazy=True, uselist = False)
    

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)