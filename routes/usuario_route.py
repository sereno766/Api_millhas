from flask import Blueprint, jsonify, request
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
# adicionar um novo cliente
@usuario_route.route("/clientes", methods=["POST"])
def post_cliente():
    dados = request.get_json()
    novo_id = adicionar_cliente(dados)
    return jsonify({"id_cliente": novo_id, "mensagem": "Cliente adicionado com sucesso!"}), 201

# retornar um cliente pelo ID
@usuario_route.route("/clientes/<int:id_usuario>", methods=["GET"])
def get_cliente(id_usuario):
    cliente = buscar_cliente(id_usuario)
    return jsonify(cliente)