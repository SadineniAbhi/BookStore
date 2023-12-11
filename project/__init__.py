from flask import Flask
from instance.config import Config
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
from project.extensions import db
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    jwt = JWTManager(app)
    
    bcrypt.init_app(app)
    # Initialize Flask extensions here
    from .models.user_model import User
    from .models.book_model import Book
    from .models.address_model import Address
    from .models.cart_model import Cart
    from .models.login_model import Login
    from .models.order_model import Order
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register blueprints here
    from project.auth import bp as authentication_blueprint
    app.register_blueprint(authentication_blueprint)
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app