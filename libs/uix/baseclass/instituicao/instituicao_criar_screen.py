from kivymd.uix.screen import MDScreen

class InstituicaoCriarScreen(MDScreen):
    """
    Example Screen
    """
    def inserir_dados(self):
        nome_fantasia = self.ids.nome_fantasia.text
        razao_social = self.ids.razao_social.text
        cie = self.ids.cie.text
        cnpj = self.ids.cnpj.text
        tipo_instituicao = self.ids.tipo_instituicao.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        email = self.ids.email.text
        contato = self.ids.contato.text
        fone_contato_i = self.ids.fone_contato_i.text
        fone_contato_ii = self.ids.fone_contato_ii.text
        logradouro = self.ids.logradouro.text
        observacao = self.ids.observacao.text

        self.dados.put(nome_fantasia, nome_fantasia=nome_fantasia,razao_social=razao_social,cie=cie,
        cnpj=cnpj,tipo_instituicao=tipo_instituicao,
        fone_i=fone_i,fone_ii=fone_ii,email=email,
        contato=contato,fone_contato_i=fone_contato_i,fone_contato_ii=fone_contato_ii,
        logradouro=logradouro,observacao=observacao)

        if self.dados.exists(nome_fantasia):
            return True