from flask import Blueprint
bp = Blueprint("address_blueprint",__name__)

from project.address import add_address
from project.address import del_address
from project.address import get_countries
from project.address import get_states_of_country