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
@usuario_route.route("/clientes/<int:id_cliente>", methods=["GET"])
def get_cliente(id_cliente):
    cliente = buscar_cliente(id_cliente)
    return jsonify(cliente)
# atualizar um cliente pelo ID
@usuario_route.route("/clientes/<int:id_cliente>", methods=["PUT"])
def put_cliente(id_cliente):
    dados = request.get_json()
    dados['id_cliente'] = id_cliente
    update_cliente(dados)
    return jsonify({"mensagem": "Cliente atualizado com sucesso!"}), 200
# deletar um cliente pelo ID
@usuario_route.route("/clientes/<int:id_cliente>", methods=["DELETE"])
def delet_cliente(id_cliente):
    deletar_cliente(id_cliente)
    return jsonify({"mensagem": "Cliente deletado com sucesso!"}), 200
# adicionar milhas a um cliente pelo ID
@usuario_route.route("/clientes/<int:id_cliente>/adicionar-milhas", methods=["POST"])
def adicionar_milhas_cliente(id_cliente):
    dados = request.get_json()
    milhas = dados.get("milhas", 0) 
    adicionar_milhas(id_cliente, milhas)
    return jsonify({"mensagem": f"{milhas} milhas adicionadas ao cliente {id_cliente}"}), 200