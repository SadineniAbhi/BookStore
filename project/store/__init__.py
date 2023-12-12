from flask import Blueprint

bp = Blueprint("store_blueprints",__name__)

from project.store import get_all_books