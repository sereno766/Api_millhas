from conn import conectar
from models.usuario_model import Cliente



def listar_clientes():
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = [Cliente(*c).__dict__ for c in cursor.fetchall()]
        cursor.close()
        con.close()
        return clientes
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
        return False

def buscar_cliente(id_cliente):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s", (id_cliente,))
        c = cursor.fetchone()
        cursor.close()
        con.close()
        return Cliente(*c).__dict__ if c else None
    except Exception as e:
        print(f"Erro ao buscar cliente: {e}")
        return False

def adicionar_cliente(dados):
    try:
        # Validação de campos obrigatórios
        campos = ['nome', 'email', 'cartao', 'saldo_milhas', 'destino_desejado']
        if not all(dados.get(campo) for campo in campos):
            print("Campos obrigatórios ausentes.")
            return False

        # Validação de saldo
        if int(dados['saldo_milhas']) < 0:
            print("Saldo de milhas não pode ser negativo.")
            return False

        # Validação de e-mail único
        con = conectar()
        cursor = con.cursor()
        cursor.execute("SELECT 1 FROM cliente WHERE EMAIL = %s", (dados['email'],))
        if cursor.fetchone():
            print("E-mail já cadastrado.")
            cursor.close()
            con.close()
            return False

        # Inserção
        sql = """
            INSERT INTO cliente (NOME, EMAIL, CARTAO, SALDO_MILHAS, DESTINO_DESEJADO)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            dados['nome'],
            dados['email'],
            dados['cartao'],
            dados['saldo_milhas'],
            dados['destino_desejado']
        )
        cursor.execute(sql, valores)
        con.commit()
        novo_id = cursor.lastrowid
        cursor.close()
        con.close()
        return novo_id
    except Exception as e:
        print(f"Erro ao adicionar cliente: {e}")
        return False

def update_cliente(dados):
    try:
        con = conectar()
        cursor = con.cursor()
        sql = """
            UPDATE cliente
            SET NOME = %s, EMAIL = %s, CARTAO = %s, SALDO_MILHAS = %s, DESTINO_DESEJADO = %s
            WHERE ID_cliente = %s
        """
        valores = (
            dados['nome'],
            dados['email'],
            dados['cartao'],
            dados['saldo_milhas'],
            dados['destino_desejado'],
            dados['id_cliente']
        )
        cursor.execute(sql, valores)
        con.commit()
        cursor.close()
        con.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        return False

def deletar_cliente(id_cliente):
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        con.commit()
        cursor.close()
        con.close()
        return True
    except Exception as e:
        print(f"Erro ao deletar cliente: {e}")
        return False

def adicionar_milhas(id_cliente, milhas):
    try:
        if int(milhas) <= 0:
            print("Milhas a adicionar deve ser maior que zero.")
            return False
        con = conectar()
        cursor = con.cursor()
        cursor.execute("UPDATE cliente SET SALDO_MILHAS = SALDO_MILHAS + %s WHERE ID_cliente = %s", (milhas, id_cliente))
        con.commit()
        cursor.close()
        con.close()
        return True
    except Exception as e:
        print(f"Erro ao adicionar milhas: {e}")
        return False
