from conn import conectar

def listar_clientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cliente")
    clientes = cursor.fetchall()
    cursor.close()
    con.close()
    return clientes

def buscar_cliente(id_cliente):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    con.close()
    return cliente

def adicionar_cliente(dados):
    con = conectar()
    cursor = con.cursor()
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