import mysql.connector

def criar_conexao(host, usuario, senha, banco_dados):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco_dados)


def fechar_conexao(con):
    return con.close()
