#quatro pilhas as mesas
#tres filas caixas e fila de entrada

class restaurante:
    def __init__(self):
        self.entrada = []
        self.mesas = [[], [], [], []]
        self.caixas = [[], []]
        self.tempo_preparo = 5

    def consulta_status_lista_espera (self):
        if len(self.lista_espera) == 0:
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
            if len(mesa) != 0:
                return self.mesas.index(mesa)
        return None

    def ocupa_mesa (self, cliente):
        mesa = consulta_mesa()
        self.mesas[mesa] = cliente

    def libera_mesa (self, mesa):
        self.mesas[mesa] = []
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
