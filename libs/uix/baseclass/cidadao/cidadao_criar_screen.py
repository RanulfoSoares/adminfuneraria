from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore


class CidadaoCriarScreen(MDScreen):
    """
    Example Screen
    """
    dados = JsonStore('hello.json')
    
    def inserir_dados(self):
        nome = self.ids.nome.text
        cpf = self.ids.cpf.text
        rg = self.ids.rg.text
        certidao_nascimento = self.ids.certidao_nascimento.text
        rne = self.ids.rne.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        sexo = self.ids.sexo.text

        self.dados.put(nome, nome=nome,cpf=cpf,rg=rg,
        certidao_nascimento=certidao_nascimento,rne=rne,
        fone_i=fone_i,fone_ii=fone_ii,sexo=sexo)

        if self.dados.exists(cpf):
            return True