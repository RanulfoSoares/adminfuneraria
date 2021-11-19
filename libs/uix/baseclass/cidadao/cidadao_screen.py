from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.screen import MDScreen


class CidadaoScreen(MDScreen):
    """
    Example Screen.
    """
    dados = JsonStore('hello.json')
    
    def filtro(self, item):
        self.ids.dados.opacity = 1
        self.ids.buscar.opacity = 1
        
        if item == 'nome':
            self.ids.dados.hint_text = 'Digite seu nome'
        if item == 'cpf':
            self.ids.dados.hint_text = 'Digite seu cpf'
        if item == 'rg':
            self.ids.dados.hint_text = 'Digite seu rg'
        if item == 'rne':
            self.ids.dados.hint_text = 'Digite rne'
            self.ids.dados.helper_text = 'Registro nacion de estrangeiro'
        if item == 'cert. nasc':
            self.ids.dados.hint_text = 'Digite sua cert. nasc.'
    def search(self):
        text = self.ids.dados.text
        self.ids.erro.opacity = 1
        if self.dados.exists(text):
            self.ids.erro.text = self.dados.get(text)['nome']
            self.ids.info.opacity = 1
            return
        
        self.ids.info.opacity = 0
        self.ids.erro.text = 'Informaçao Nao Encontrada'


    def abrir(self):
        opcoes = ['nome','cpf', 'rg', 'rne', 'cert. nasc']
        menu_items = [
            {
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.filtro(x)
            } for index in range(len(opcoes))
            ]
        self.menu = MDDropdownMenu(
            caller=self.ids.toolbar,
            items= menu_items,
            width_mult=2
        )
        self.menu.open()
