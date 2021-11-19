from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

class LoginScreen(Screen):
    """
    esta e uma tela de login
    """
    dados = JsonStore('auth.json')
    def login(self):
        cpf =  self.ids.cpf.text
        senha = self.ids.senha.text

        if self.dados.exists(cpf):
            user = self.dados.get(cpf)
            if user['senha'] == senha:
                return True
            print('senha errada')
            return False
        print('usuario nao encontrado')

