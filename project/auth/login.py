from project.auth import bp
from flask import jsonify,request
from flask_jwt_extended import create_access_token
from project.models.user_model import User
@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify({'msg':"invalid cred"}) , 401
    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)

