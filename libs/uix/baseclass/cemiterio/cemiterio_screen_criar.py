from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore


class CemiterioCriarScreen(MDScreen):
    """
    Example Screen
    """
    dados = JsonStore('hello.json')
    
    def inserir_dados(self):
        nome_legal = self.ids.nome_legal.text
        nome_fantasia = self.ids.nome_fantasia.text
        cnpj = self.ids.cnpj.text
        adm_publica_privada = self.ids.adm_publica_privada.text
        data_inauguracao = self.ids.data_inauguracao.text
        diretor_responsavel = self.ids.diretor_responsavel.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        email = self.ids.email.text
        logradouro = self.ids.logradouro.text
        bairro = self.ids.bairro.text
        cidade = self.ids.cidade.text
        observacao = self.ids.observacao.text

        self.dados.put(nome_legal, nome_legal=nome_legal,nome_fantasia=nome_fantasia,
        cnpj=cnpj,adm_publica_privada=adm_publica_privada,data_inauguracao=data_inauguracao,
        didretor_responsavel=diretor_responsavel,fone_i=fone_i,fone_ii=fone_ii,
        email=email,logradouro=logradouro,bairro=bairro,cidade=cidade,observacao=observacao)

        if self.dados.exists(cpf):
            return True