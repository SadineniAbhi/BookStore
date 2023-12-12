from project.auth import bp
from flask import jsonify,request
from flask_jwt_extended import create_access_token
from services.auth_services.get_attempted_user import getuser
@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = getuser(username)
    if not user or not user.check_password(password):
        return jsonify({'msg':"invalid cred"}) , 401
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)

