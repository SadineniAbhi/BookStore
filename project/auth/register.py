from project.auth import bp
from flask import request,jsonify
import datetime
from project import bcrypt
from services.user_services.add_user import add_user
from project.models.user_model import User

@bp.route("/register",methods = ["POST"])
def register():
    username = request.json.get("username",None)
    email = request.json.get("email",None)
    password = request.json.get("password", None)
    last_updated_by = username
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        add_user(username,email,hashed_password,last_updated_by)
        return {"msg":'created user'}
    except:
        return {"msg":'unable to create user'}
    
        