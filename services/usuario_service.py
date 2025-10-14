from conn import conectar

def listar_clientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM USUARIO")
    clientes = cursor.fetchall()
    cursor.close()
    con.close()
    return clientes

def buscar_cliente(id_usuario):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM USUARIO WHERE id_usuario = %s", (id_usuario,))
    cliente = cursor.fetchone()
    cursor.close()
    con.close()
    return cliente