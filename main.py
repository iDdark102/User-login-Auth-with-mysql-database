

from Connect import criar_conexao,fechar_conexao
import PySimpleGUI as pg
class main_class:
    def __init__(self):
        self.con = criar_conexao('localhost', 'root', 'senha_banco_root', 'cadastro')
        self.logado = False
        self.cursor = self.con.cursor()
        self.cursor.close()
        self.helper = ''

    def consultar(self):
        fechar_conexao(self.con)
        self.con = criar_conexao('localhost', 'root', 'senha_banco_root', 'cadastro')
        self.cursor = self.con.cursor()
        comando = '''select * from usuarios;'''
        self.cursor.execute(comando)
        lista = []
        for i in self.cursor:
            lista.append(i)
        for i in lista:
            print(i)
        self.cursor.close()
        return lista
    def cadastrar(self, login,senha,nome,email):
        self.cursor = self.con.cursor()
        lista = login.split()
        while len(lista)>1:
            if len(lista) >1 or len(lista[0])>30:
                return 'O login não pode ter espaços e ter no máximo 30 caracteres.'
        lista = senha.split()
        while len(lista)>1:
            if len(lista) >1 or len(lista[0])>30:
                return 'A senha não pode ter espaços e ter no máximo 30 caracteres.'
        comando = '''
        insert into usuarios
        (id,login,senha,nome,email)
        values (DEFAULT, '{}', '{}','{}','{}');'''
        self.cursor.execute(comando.format(login,senha,nome,email))
        self.con.commit()
        self.cursor.close()
        return 'Usuário cadastrado!'
    def deletar_usuario(self,login, senha):
        consultar_usuarios = conectar.consultar()
        for i in consultar_usuarios:
            if login in i:
                if senha == i[2]:
                    self.cursor = self.con.cursor()
                    self.cursor.execute(f'DELETE FROM usuarios WHERE id={i[0]};')
                    self.con.commit()
                    self.cursor.close()
                    return 'Conta deletada!'
    def logar(self, login, senha):
        consultar_usuarios = conectar.consultar()
        logou = False
        for i in consultar_usuarios:
            if login == i[1]:
                if senha==i[2]:
                    self.logado = i
                    logou = True
                    break
        if not logou:
            self.logado = False
        return self.logado


conectar = main_class()
