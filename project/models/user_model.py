from project.extensions import db
import datetime
from datetime import datetime
from project import bcrypt
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_date_time = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated_by = db.Column(db.String(20),nullable = False)

    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)