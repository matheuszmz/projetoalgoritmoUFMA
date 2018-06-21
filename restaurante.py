import time

class restaurante:
    def __init__(self):
        self.entrada = 1
        self.mesas = [0, 0, 0, 0]
        self.caixas = [0, 0]
        self.lista_espera = []

    def consulta_status_lista_espera (self):
        tamanho_fila = len(self.lista_espera)
        if tamanho_fila == 0:
            return False
        else:
            return True

    def adiciona_cliente_lista_espera (self):
        self.lista_espera.append('x')

    def remove_cliente_lista_espera (self):
        self.lista_espera.pop(0)

    def acomoda_cliente_lista_espera(self):
        ocupa_mesa()
        remove_cliente_lista_espera()

    def consulta_mesa (self):
        for mesa in self.mesas:
            if mesa == 0:
                return self.mesas.index(mesa)
        return None

    def ocupa_mesa (self):
        mesa = consulta_mesa()
        self.mesas[mesa] = 1

    def libera_mesa (self, mesa):
        self.mesas[mesa] = 0
        if consulta_status_lista_espera() == True:
            acomoda_cliente_lista_espera()
        
    def recepciona_cliente(self):
        if consulta_status_lista_espera() == False:
            if consulta_mesa == None:
                adiciona_cliente_lista_espera()
            else:
                ocupa_mesa()
        else:
            adiciona_cliente_lista_espera()
