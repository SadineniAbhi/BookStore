from flask import Flask
from instance.config import Config
from flask_bcrypt import Bcrypt
from project.extensions import db,bcrypt,jwt
from project.models.user_model import User

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    #add models here
    from .models.user_model import User
    from .models.book_model import Book
    from .models.address_model import Address
    from .models.cart_model import Cart
    from .models.login_model import Login
    from .models.order_model import Order
    # Initialize Flask extensions here
    jwt.init_app(app)
    bcrypt.init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Register blueprints here
    from project.auth import bp as authentication_blueprint
    app.register_blueprint(authentication_blueprint)
    from project.admin import bp as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from project.store import bp as store_blueprint
    app.register_blueprint(store_blueprint)

    from project.address import bp as address_blueprint
    app.register_blueprint(address_blueprint)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'
    
    return app

