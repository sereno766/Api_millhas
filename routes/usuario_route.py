from flask import Blueprint
from services.usuario_service import *


usuario_route = Blueprint('usuario_route', __name__)



@usuario_route.route("/")
def hello():
    return "Tudo OK!"


