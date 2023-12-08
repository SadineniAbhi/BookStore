from flask import Flask
import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/bookstore'
db = SQLAlchemy()
db.init_app(app)
from project.Books.Book_Model import Book



