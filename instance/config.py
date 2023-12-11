import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/bookstore'
    SQLALCHEMY_TRACK_MODIFICATIONS = False