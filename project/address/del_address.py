from project.address import bp 
from project.models.address_model import Address
from services.address_services.delete_address import del_add
from flask import jsonify,request,json
from project import db
from flask_jwt_extended import jwt_required

@bp.route("/del_address",methods = ["POST"])
@jwt_required()
def del_address():
    address_id = request.json.get("address_id")
    try:
        del_add(address_id)
        return {"msg":"deleted address"}
    except:
        return {"msg":"unable to del address"}