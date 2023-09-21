import sqlite3


def cadastra_usuario(nome, idade, cpf, endereco, email):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()

    if idade < 0 or idade > 120:
        return False
    
    if len(cpf) != 11:
        return False
    
    if "@" in email:
        partes = email.split("@")
        if len(partes) != 2 or len(partes[0]) == 0 or len(partes[1]) == 0:
            return False
    
    if "@" not in email:
        return False

    cursor.execute(f"""
    INSERT INTO Usuarios (nome, idade, cpf, endereco, email)
    VALUES ('{nome}', {idade}, '{cpf}', '{endereco}', '{email}')
    """)

    conn.commit()
    conn.close()

    return True

def busca_usuario(id):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    SELECT * FROM Usuarios WHERE id = {id}
    """)

    usuario = cursor.fetchone()

    conn.close()

    return usuario

def busca_usuarios():
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    SELECT * FROM Usuarios
    """)

    usuarios = cursor.fetchall()

    conn.close()

    return usuarios

def atualiza_usuario(id, nome, idade, cpf, endereco, email):
    conn = sqlite3.connect('db/e_magic_shop_v2.db')
    cursor = conn.cursor()

    if idade < 0 or idade > 120:
        return False
    
    if len(cpf) != 11:
        return False
    
    if "@" in email:
        partes = email.split("@")
        if len(partes) != 2 or len(partes[0]) == 0 or len(partes[1]) == 0:
            return False
    
    if "@" not in email:
        return False

    if busca_usuario(id) is None:
        return None

    cursor.execute(f"""
    UPDATE Usuarios SET nome = '{nome}', idade = {idade}, cpf = '{cpf}', endereco = '{endereco}', email = '{email}'
    WHERE id = {id}
    """)

    conn.commit()
    conn.close()

    return True
