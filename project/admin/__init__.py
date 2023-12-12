from flask import Blueprint

bp = Blueprint("admin",__name__)

from project.admin import addbooks
from project.admin import delete_book
from project.admin import update_books_quantity