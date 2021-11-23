from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore

class UsuarioCriarScreen(MDScreen):
    """
    Example Screen
    """

    dados = JsonStore('hello.json')
    
    def inserir_dados(self):
        nome_usuario = self.ids.nome_usuario.text
        nome_usual = self.ids.nome_usual.text
        senha_i = self.ids.senha_i.text
        senha_ii = self.ids.senha_ii.text
        cpf = self.ids.cpf.text
        rg = self.ids.rg.text
        certidao_nascimento = self.ids.certidao_nascimento.text
        rne = self.ids.rne.text
        data_nascimento = self.ids.data_nascimento.text
        idade = self.ids.idade.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        sexo = self.ids.sexo.text
        cor = self.ids.cor.text
        escolaridade = self.ids.escolaridade.text
        situacao_matrimonial = self.ids.situacao_matrimonial.text
        email = self.ids.email.text
        funcao = self.ids.funcao.text
        data_admissao = self.ids.data_admissao.text
        data_desligamento = self.ids.data_desligamento.text
        logradouro = self.ids.logradouro.text


        self.dados.put(nome_usuario, nome_usuario=nome_usuario,
        nome_usual=nome_usual,senha_i=senha_i,senha_ii=senha_ii,
        cpf=cpf,rg=rg,certidao_nascimento=certidao_nascimento,rne=rne,
        data_nascimento=data_nascimento,idade=idade,fone_i=fone_i,
        fone_ii=fone_ii,sexo=sexo,cor=cor,escolaridade=escolaridade,
        situacao_matrimonial=situacao_matrimonial,email=email,funcao=funcao,
        data_admissao=data_admissao,data_desligamento=data_desligamento,
        logradouro=logradouro)       
        

        if self.dados.exists(nome_usuario):
            return True