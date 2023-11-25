import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



#sets the app
app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"
#security
login_manager = LoginManager(app)
login_manager.login_view = "login"
bcrypt = Bcrypt(app)


##################################################
#####################SQL DATABASE ################
##################################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#reads and updates the changes in the database design
Migrate(app,db)

from project.routes import buying_page, admin_routes,login_register, previous_orders, storepage
