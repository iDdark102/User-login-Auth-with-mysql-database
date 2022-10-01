import PySimpleGUI as sg
from main import main_class

sg.theme('DarkBlack')
class sistema:
    def __init__(self):
        self.mensagem = ''
    def tela_inicial(self, mensagem):
        layout_tela_inicial = [
            [sg.Text('')],
            [sg.Text('Sistema de autenticação de login com banco de dados MySQL criado por Gabriel Macêdo de Araújo.')],
            [sg.Text('')],
            [sg.Text('',size=25),sg.Button('Logar'), sg.Text('', size=5), sg.Button('Registrar')],
            [sg.Text(mensagem,text_color='Red')]
        ]

        janela = sg.Window('Autenticação de login', resizable=True).layout(layout_tela_inicial)
        Botao, valores = janela.Read()
        janela.close()
        return Botao


    def tela_login(self):
        layout_login = [
            [sg.Text('Login:', size=7), sg.Input(key='login')],
            [sg.Text('Senha:', size=7), sg.Input(key='senha')],
            [sg.Button('Entrar')]
        ]

        janela = sg.Window('Autenticação de login', resizable=True).layout(layout_login)
        Botao, valores = janela.Read()
        if Botao == 'Entrar':
            if conectar.logar(valores['login'], valores['senha']):
                self.mensagem = ''
                janela.close()
                return True

            else:
                self.mensagem = 'Credenciais inválidas! Tente novamente ou registre-se'
                janela.close()
                return False
        else:
            self.mensagem = ''
            janela.close()
    def tela_cadastro(self):
        layout_cadastro = [
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('Email:'), sg.Input(key='email')],
            [sg.Text('Login:'), sg.Input(key='login')],
            [sg.Text('Senha:', size=25), sg.Input(key='senha')],
            [sg.Text('Digite a senha novamente:', size=25), sg.Input(key='senha_confirm')],
            [sg.Button('Cadastrar')]
        ]

        janela = sg.Window('Autenticação de login', resizable=True).layout(layout_cadastro)
        Botao, valores = janela.Read()

        if Botao == 'Cadastrar':
            if valores['senha'] == valores['senha_confirm']:
                janela.close()
                self.mensagem = ''
                return conectar.cadastrar(valores['login'],valores['senha'])
            else:
                janela.close()
                self.mensagem = 'As senhas não coincidem!'
        else:
            janela.close()
            self.mensagem = ''
sistema = sistema()
conectar = main_class()
while True:
    mensagem = sistema.mensagem
    action = sistema.tela_inicial(mensagem)
    if action == 'Logar':
        if sistema.tela_login():
            print('logado')
    elif action == 'Registrar':
        if sistema.tela_cadastro():
            print('cadastrado')
    else:
        break
from Connect import fechar_conexao
fechar_conexao(conectar.con)