from kivymd.uix.screen import MDScreen
from kivy.storage.jsonstore import JsonStore
class JazigoCriarScreen(MDScreen):
    """
    Example Screen
    """
    dados = JsonStore('hello.json')
    
    def inserir_dados(self):
        rua = self.ids.rua.text
        quadra = self.ids.quadra.text
        setor = self.ids.setor.text
        jazigo = self.ids.jazigo.text
        jazigo_perpetuo_provisorio = self.ids.jazigo.text
        comprador_jazigo = self.ids.jazigo.text
        jazigo_valor_pago = self.ids.jazigo.text
        sepultamento_valor_pago = self.ids.jazigo.text
        valor_total_pago = self.ids.jazigo.text
        recibo_pagto_numero = self.ids.jazigo.text
        observacao = self.ids.jazigo.text

        self.dados.put(jazigo, jazigo=jazigo,rua=rua,quadra=quadra,
        setor=setor,comprador_jazigo=comprador_jazigo,jazigo_valor_pago=jazigo_valor_pago,
        sepultamento_valor_pago=sepultamento_valor_pago,
        valor_total_pago=valor_total_pago,recibo_pagto_numero=recibo_pagto_numero,
        observacao=observacao,jazigo_perpetuo_provisorio=jazigo_perpetuo_provisorio)

        if self.dados.exists(jazigo):
            return True
        