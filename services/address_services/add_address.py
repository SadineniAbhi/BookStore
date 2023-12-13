from project.models.address_model import Address
from flask_jwt_extended import current_user
from project import db

def addAddress(flat_no,house_no,street_name,city_name,country_id,state_id):
    newAddress = Address(flat_no = flat_no, house_no = house_no, 
                         street_name = street_name, city_name = city_name,
                        country_id =country_id, state_id = state_id)
    db.session.add(newAddress)
    db.session.commit()