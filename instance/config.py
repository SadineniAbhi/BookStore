class Config:
    SECRET_KEY = "mykey"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/bookstore'
    SQLALCHEMY_TRACK_MODIFICATIONS = False