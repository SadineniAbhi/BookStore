from flask import Blueprint

bp = Blueprint('authentication',__name__)

import project.auth.login
import project.auth.register