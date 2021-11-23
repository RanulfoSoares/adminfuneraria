from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class CemiterioInfoScreen(MDScreen):
    """
    Example Screen
    """
    nome_legal = StringProperty()
    nome_fantasia = StringProperty()
    cnpj = StringProperty()
    adm_publica_privada = StringProperty()
    data_inauguracao = StringProperty()
    diretor_responsavel = StringProperty()
    fone_i = StringProperty()
    fone_ii = StringProperty()
    email = StringProperty()    
    logradouro = StringProperty()
    bairro = StringProperty()
    cidade = StringProperty()
    observacao = StringProperty()

    nome_legal = 'example'
    nome_fantasia = 'example'
    cnpj = 'example'
    adm_publica_privada = 'example'
    data_inauguracao = 'example'
    diretor_responsavel = 'example'
    fone_i = 'example'
    fone_ii = 'example'
    email = 'example'
    logradouro = 'example'
    bairro = 'example'
    cidade = 'example'
    observacao = 'example'