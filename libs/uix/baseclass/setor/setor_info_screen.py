from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class SetorInfoScreen(MDScreen):
    """
    Example Screen
    """

    nome_setor = StringProperty()
    tipo_setor = StringProperty()
    fone_i = StringProperty()
    fone_ii = StringProperty()
    email = StringProperty()
    contato = StringProperty()
    fone_contato_i = StringProperty()
    fone_contato_ii = StringProperty()
    observacao = StringProperty()
    logradouro = StringProperty()    

    nome_setor = 'example'
    tipo_setor = 'example'
    fone_i = 'example'
    fone_ii = 'example'
    email = 'example'
    contato = 'example'
    fone_contato_i = 'example'
    fone_contato_ii = 'example'
    observacao = 'example'
    logradouro = 'example'
