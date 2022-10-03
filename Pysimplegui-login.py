import PySimpleGUI as sg
from main import main_class

sg.theme('DarkBlack')
class sistema:
    def __init__(self):
        self.mensagem = ''
        self.user = ''
        self.nome = ''
        self.email = ''
        self.login = ''
    def tela_inicial(self, mensagem):
        layout_tela_inicial = [
            [sg.Text('')],
            [sg.Text('Sistema de autenticação de login com banco de dados MySQL.')],
            [sg.Text('')],
            [sg.Text('',size=12),sg.Button('Logar'), sg.Text('', size=5), sg.Button('Registrar')],
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
            lista = conectar.logar(valores['login'], valores['senha'])
            if lista:
                self.login = valores['login']
                self.nome = lista[3]
                self.email = lista[4]
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
            [sg.Button('Cadastrar',bind_return_key=True)]
        ]

        janela = sg.Window('Autenticação de login', resizable=True).layout(layout_cadastro)
        Botao, valores = janela.Read()

        if Botao == 'Cadastrar':
            if valores['nome'] != '' and valores['email']!='' and valores['login']!='':
                if valores['senha'] == valores['senha_confirm']:
                    janela.close()
                    self.mensagem = ''
                    return conectar.cadastrar(valores['login'],valores['senha'],valores['nome'],valores['email'])
                else:
                    janela.close()
                    self.mensagem = 'As senhas não coincidem!'
            else:
                self.mensagem = 'Preencha todos os campos obrigatórios!'
                janela.close()
        else:
            janela.close()
            self.mensagem = ''

    def pagina_inicial_logado(self):
        layout = [
            [sg.Text('{}'.format(self.login),text_color='Orange'),sg.Text('online',text_color='Green')],
            [sg.Text('Nome:',text_color='White'),sg.Text('{}'.format(self.nome),text_color='Orange')],
            [sg.Text('E-mail:', text_color='White'), sg.Text('{}'.format(self.email), text_color='Orange')],
            [sg.Text('Página inicial, usuário com permissões de {}'.format('convidado'))],
            [sg.Button('Deslogar')]
        ]

        janela = sg.Window('Página inicial').layout(layout)
        Botao, valores = janela.Read()
        if Botao == 'Deslogar':
            janela.close()
            return False
        else:
            return True
sistema = sistema()
conectar = main_class()
while True:
    logado = False
    mensagem = sistema.mensagem
    action = sistema.tela_inicial(mensagem)
    if action == 'Logar':
        if sistema.tela_login():
            logado = True
    elif action == 'Registrar':
        if sistema.tela_cadastro():
            print('cadastrado')
    else:
        break
    if logado:
        sistema.pagina_inicial_logado()


from Connect import fechar_conexao
fechar_conexao(conectar.con)
