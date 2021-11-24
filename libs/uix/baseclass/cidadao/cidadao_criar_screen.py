from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.menu.menu import MDDropdownMenu
from kivy.network.urlrequest import UrlRequest

estados_opcoes = []
pais_opcoes = []
banco_estados = JsonStore('banco/estados.json')
banco_pais = JsonStore('banco/pais.json')
banco_cidades = JsonStore('banco/cidades.json')



class CidadaoCriarScreen(MDScreen):
    """
    Example Screen
    """
    
    def data_pais(req, result):
        for pais in result:
            banco_pais.put(pais['nome'])
    
    def data_estado(req, result):
        for estado in result:
            banco_estados.put(estado['nome'], id=estado['id'])
        
    #url = UrlRequest('https://servicodados.ibge.gov.br/api/v1/localidades/estados', on_success=data_estado)
    

    
    nomes = banco_estados.keys()
    paises = banco_pais.keys()
    estados = banco_estados.keys()

    def abrir_bairro(self):

        menu_item = [
            {
                'text': cidades[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{cidades[index]}' : self.cidade_filtro(x)
            } for index in range(len(cidades))
        ]
        menu = MDDropdownMenu(
            caller=self.ids.cidade,
            items= menu_item,
            width_mult=4
        )
        menu.open()

    def cidade_filtro(self, cidade):
        self.cidade = cidade
        self.ids.cidade.text = cidade

    def abrir_menu_cidade(self):
        cidades = banco_cidades.keys()
        menu_item = [
            {
                'text': cidades[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{cidades[index]}' : self.cidade_filtro(x)
            } for index in range(len(cidades))
        ]
        menu = MDDropdownMenu(
            caller=self.ids.cidade,
            items= menu_item,
            width_mult=4
        )
        menu.open()
    
    def estado_filtro(self, estado):
        def data_cidade(req, result):
            for cidade in result:
                banco_cidades.put(cidade['nome'], id=cidade['id'])
        self.estado = estado
        self.ids.estado.text = str(self.estado)
        estado_data = banco_estados.get(str(self.estado))
        estado_selecionado = estado_data['id']
        url = UrlRequest(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/${estado_selecionado}/municipios', on_success=data_cidade)
        

    def abrir_menu_estado(self):
        menu_item = [
            {
                'text': self.nomes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{self.nomes[index]}' : self.estado_filtro(x)
            } for index in range(len(self.nomes))
        ]
        menu = MDDropdownMenu(
            caller=self.ids.estado,
            items= menu_item,
            width_mult=4
        )
        menu.open()
    def pais_filtro(self, pais):
        self.pais = pais
        self.ids.nacionalidade.text = str(self.pais)
    def abrir_paises(self):
        menu_item = [
            {
                'text': self.paises[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{self.paises[index]}' : self.pais_filtro(x)
            } for index in range(len(self.paises))
        ]
        menu = MDDropdownMenu(
            caller=self.ids.nacionalidade,
            items=menu_item,
            width_mult=4
        )
        menu.open()

    
    dados = JsonStore('hello.json')
    sexo = None
    estado_civil = None
    cor = None
    escolaridade = None
    
    def sexo_filtro(self, sexo):
        self.sexo = sexo
        self.ids.sexo.text = str(sexo)
    def sexo(self):
        opcoes = ['heterossexual', 'homossexual', 'bissexual','assexual', 'masculino', 'feminino']
        menu_items = [{
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.sexo_filtro(x)
            } for index in range(len(opcoes))]
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

    def cor_filtro(self, cor):
        self.cor = cor
        self.ids.cor.text = str(cor)
    def cor(self):
        opcoes = ['Amarela', 'Branca', 'Indígena','Parda', 'Preta']
        menu_items = [{
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.cor_filtro(x)
            } for index in range(len(opcoes))]
        self.menu = MDDropdownMenu(
            caller=self.ids.cor,
            items= menu_items,
            width_mult=4
        )
        self.menu.open()

    def escolaridade_filtro(self, escolaridade):
        self.escolaridade = escolaridade
        self.ids.escolaridade.text = str(escolaridade)
    def escolaridade(self):
        opcoes = ['1º Ensino fundamental', '1º Ensino médio', '2º Ensino fundamental', '2º Ensino médio', 
        '3º Ensino fundamental','3º Ensino médio','4º Ensino fundamental', '5º Ensino fundamental',
        '6º Ensino fundamental', '7º Ensino fundamental','8º Ensino fundamental','9º Ensino fundamental',
        'APAE','Creche','Desconhecido','EJA','Ensino médio completo','Não estuda','Não se aplica',
        'Pós-graduado','Pré-escola','Superior','Superior incompleto','Supletivo','']
        menu_items = [
            {
                'text': opcoes[index],
                "viewclass": "OneLineListItem",
                'on_release': lambda x = f'{opcoes[index]}' : self.escolaridade_filtro(x)
            } for index in range(len(opcoes))
            ]
        self.menu = MDDropdownMenu(
            caller=self.ids.escolaridade,
            items= menu_items,
            width_mult=4
        )
        self.menu.open()
    
    def inserir_dados(self):
        try:
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
            nacionalidade = self.ids.nacionalidade.text
            escolaridade = self.ids.escolaridade.text
            estado = self.ids.estado.text
            cidade = self.ids.cidade.text
            bairro = self.ids.bairro.text
            logradouro = self.ids.logradouro.text
            cep = self.ids.cep.text
            cor  = self.ids.cor.text
            complemento = self.ids.complemento.text

            if nome == None and apelido == None and cpf == None and rg == None and certidao_nascimento == None and rne == None and escolaridade == None and fone_i == None and fone_ii == None and sexo == None and estado_civil == None and nacionalidade == None and escolaridade == None and estado == None and cidade == None and bairro == None and logradouro == None and cep == None and cor == None:
                return False

            self.dados.put(nome, nome=nome,apelido=apelido,cpf=cpf,rg=rg,
            certidao_nascimento=certidao_nascimento,rne=rne,estado_civil=estado_civil,
            fone_i=fone_i,fone_ii=fone_ii,sexo=sexo, estado=estado,cidade=cidade,
            bairro=bairro,logradouro=logradouro, cep=cep,cor=cor,complemento=complemento,
            nacionalidade=nacionalidade,escolaridade=escolaridade)

            if self.dados.exists(cpf):
                return True
        except:
            self.ids.criar.text = 'Existe algum campo errado'
            return True
        

        