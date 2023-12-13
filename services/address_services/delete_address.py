from project.models.address_model import Address
from flask_jwt_extended import current_user
from project import db

def del_add(address_id):
    address_to_del = Address.query.get(address_id)
    db.session.delete(address_to_del)
    db.session.commit()