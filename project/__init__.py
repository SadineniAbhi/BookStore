import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # sets default settings
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/bookstore',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # deciding whether to choose test config or config.py file
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # creates an instance folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize SQLAlchemy with the app
    db.init_app(app)

    # import models here (after db initialization to avoid circular imports)
    from .models.user_model import User
    from .models.book_model import Book
    from .models.address_model import Address
    from .models.cart_model import Cart
    from .models.login_model import Login
    from .models.order_model import Order
    

    # create tables using Flask-Migrate
    # This is just an example, you would run "flask db upgrade" from the command line
    # after setting up and running migrations.
    # For more details, refer to Flask-Migrate documentation.
    # migrate.init_app(app, db)
    
    with app.app_context():
        # Access the database within the application context
        db.create_all()

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

