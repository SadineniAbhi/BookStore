from project.address import bp 
from project.models.address_model import Address
from services.address_services.add_address import addAddress
from flask import jsonify,request,json
from project import db
from flask_jwt_extended import jwt_required

@bp.route("/add_address",methods = ["GET","POST"])
@jwt_required()
def add_address():
    house_no = request.json.get("house_no",None)
    flat_no = request.json.get("flat_no",None)
    street_name = request.json.get("street_name",None)
    city_name = request.json.get("city_name",None)
    country_id = request.json.get("country_id",None)
    state_id = request.json.get("state_id",None)
    try:
        addAddress(house_no=house_no,flat_no=flat_no,street_name=street_name,
                            city_name=city_name,state_id=state_id,country_id=country_id)
        return {"msg":"added address"}
    except:
        return {"msg":"unable to add user"}
    



