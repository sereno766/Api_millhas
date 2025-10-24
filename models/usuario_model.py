from dataclasses import dataclass


@dataclass
class Cliente:
    id_cliente: int
    nome: str
    email: str
    cartao: str
    saldo_milhas: int
    destino_desejado: str
