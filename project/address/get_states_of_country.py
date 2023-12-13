from project.address import bp 
from project.models.address_model import State
from services.address_services.get_states_of_country import getStateOfCountry
from flask import jsonify,request,json
from project import db
from flask_jwt_extended import jwt_required

@bp.route("/getallstates")
@jwt_required()
def getallstates():
    country_id = request.json.get("country_id")
    all_state_of_country = getStateOfCountry(country_id=country_id)
    statesdict = {}
    for state in all_state_of_country:
        statesdict[state.state_id] = {
            'state_name':state.state_name
        }
    return jsonify(statesdict)