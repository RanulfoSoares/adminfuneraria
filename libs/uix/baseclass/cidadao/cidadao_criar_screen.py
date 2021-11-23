from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.network.urlrequest import UrlRequest

estados_opcoes = []
banco_estados = JsonStore('banco/estados.json')
class CidadaoCriarScreen(MDScreen):
    """
    Example Screen
    """
    
    def data_estado(req, result):
        for estado in result:
            banco_estados.put(estado['nome'])
        
    url = UrlRequest('https://brasilapi.com.br/api/ibge/uf/v1', on_success=data_estado)

    nomes = banco_estados.keys()

    def abrir_menu_estado(self):
        menu_item_estado = [
            {
                'text': self.nomes[index],
                "viewclass": "OneLineListItem",
                
            } for index in range(len(self.nomes))
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.estado,
            items= menu_item_estado,
            width_mult=4
        )
        self.menu.open()
    
    dados = JsonStore('hello.json')
    sexo = None
    estado_civil = None

    def sexo_filtro(self, sexo):
        self.sexo = sexo
        self.ids.sexo.text = str(sexo)
    def sexo(self):
        opcoes = ['heterossexual', 'homossexual', 'bissexual','assexual', 'masculino', 'feminino']
        menu_items = [
            {
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.sexo_filtro(x)
            } for index in range(len(opcoes))
            ]
        self.menu = MDDropdownMenu(
            caller=self.ids.sexo,
            items= menu_items,
            width_mult=4
        )
        self.menu.open()
    
    def estado_civil_filtro(self, estado_civil):
        self.estado_civil = estado_civil
        self.ids.estado_civil.text = str(estado_civil)
    def estado_civil(self):
        opcoes = ['Amasiada(o)', 'Casada(o)', 'Divorciada(o)', 'Desconhecido', 
        'Separada(o)','Solteira(o)','Viuva(o)']
        menu_items = [
            {
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.estado_civil_filtro(x)
            } for index in range(len(opcoes))
            ]
        self.menu = MDDropdownMenu(
            caller=self.ids.estado_civil,
            items= menu_items,
            width_mult=4
        )
        self.menu.open()

    
    def inserir_dados(self):
        nome = self.ids.nome.text
        apelido = self.ids.apelido.text
        cpf = self.ids.cpf.text
        rg = self.ids.rg.text
        certidao_nascimento = self.ids.certidao_nascimento.text
        rne = self.ids.rne.text
        fone_i = self.ids.fone_i.text
        fone_ii = self.ids.fone_ii.text
        sexo = self.sexo
        estado_civil = self.ids.estado_civil.text
        estado = self.ids.estado.text
        cidade = self.ids.cidade.text
        bairro = self.ids.bairro.text
        logradouro = self.ids.logradouro.text
        cep = self.ids.cep.text
        cor  = self.ids.cor.text
        complemento = self.ids.complemento.text

        self.dados.put(nome, nome=nome,apelido=apelido,cpf=cpf,rg=rg,
        certidao_nascimento=certidao_nascimento,rne=rne,estado_civil=estado_civil,
        fone_i=fone_i,fone_ii=fone_ii,sexo=sexo, estado=estado,cidade=cidade,
        bairro=bairro,logradouro=logradouro, cep=cep,cor=cor,complemento=complemento)

        if self.dados.exists(cpf):
            return True