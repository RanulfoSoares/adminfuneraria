from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class InstituicaoInfoScreen(MDScreen):
    """
    Example Screen
    """

    nome_fantasia = StringProperty()
    razao_social = StringProperty()
    cie = StringProperty()
    cnpj = StringProperty()
    tipo_instituicao = StringProperty()
    fone_i = StringProperty()
    fone_ii = StringProperty()
    email = StringProperty()
    contato = StringProperty()
    fone_contato_i = StringProperty()
    fone_contato_ii = StringProperty()
    logradouro = StringProperty()
    observacao = StringProperty()

    nome_fantasia = 'example'
    razao_social = 'example'
    cie = 'example'
    cnpj = 'example'
    tipo_instituicao = 'example'
    fone_i = 'example'
    fone_ii = 'example'
    email = 'example'
    contato = 'example'
    fone_contato_i = 'example'
    fone_contato_ii = 'example'
    logradouro = 'example'
    observacao = 'example'