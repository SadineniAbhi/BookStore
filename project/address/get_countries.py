from project.address import bp 
from project.models.address_model import Country
from services.address_services.get_countries import getCountries
from flask import jsonify,request,json
from project import db
from flask_jwt_extended import jwt_required

@bp.route("/getcountries")
@jwt_required()
def getcountry():
    all_countires = getCountries()
    all_country_dict  = {}
    for country in all_countires:
        all_country_dict[country.id] = {
            'country_name':country.country_name
        }
    return jsonify(all_country_dict)
    