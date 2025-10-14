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