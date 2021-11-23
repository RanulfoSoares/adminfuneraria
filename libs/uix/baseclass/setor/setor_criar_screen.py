from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore


class SetorCriarScreen(MDScreen):
    """
    Example Screen
    """

    dados = JsonStore('hello.json')
    
    def inserir_dados(self):
        nome_setor = self.ids.nome_setor.text
        tipo_setor = self.ids.tipo_setor.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        email = self.ids.email.text
        contato = self.ids.contato.text
        fone_contato_i = self.ids.fone_contato_i.text
        fone_contato_ii = self.ids.fone_contato_ii.text
        observacao = self.ids.observacao.text
        logradouro = self.ids.logradouro.text

        self.dados.put(nome_setor,nome_setor=nome_setor,tipo_setor=tipo_setor,fone_i=fone_i,
        fone_ii=fone_ii,email=email,contato=contato,fone_contato_i=fone_contato_ii,
        observacao=observacao,logradouro=logradouro)

        if self.dados.exists(nome_setor):
            return True