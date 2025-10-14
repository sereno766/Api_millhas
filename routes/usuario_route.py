from flask import Blueprint, jsonify
from services.usuario_service import *


usuario_route = Blueprint('usuario_route', __name__)



@usuario_route.route("/")
def hello():
    return "Tudo OK!"

# retornar todos os clientes
@usuario_route.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = listar_clientes()
    return jsonify(clientes)



@usuario_route.route("/clientes/<int:id_usuario>", methods=["GET"])
def get_cliente(id_usuario):
    cliente = buscar_cliente(id_usuario)
    return jsonify(cliente)