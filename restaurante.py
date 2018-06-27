#quatro pilhas as mesas
#tres filas caixas e fila de entrada

class Restaurante:
    def __init__ (self):
        self.lista_espera = []
        self.mesas = [[], [], [], []]
        self.caixas = [[], []]
        self.tempo_preparo = 5

    def consulta_status_lista_espera (self):
        if len(self.lista_espera) == 0:
            return False
        else:
            return True

    def adiciona_cliente_lista_espera (self):
        self.lista_espera.append('X')

    def remove_cliente_lista_espera (self):
        self.lista_espera.pop(0)

    def acomoda_cliente_lista_espera (self, clientes):
        self.ocupa_mesa(clientes)
        self.remove_cliente_lista_espera()

    def consulta_mesa_livre (self):
        for mesa in self.mesas:
            if mesa == []:
                return self.mesas.index(mesa)
        return None

    def consulta_mesa_ocupada (self):
        for mesa in self.mesas:
            if mesa != []:
                return self.mesas.index(mesa)
        return None

    def ocupa_mesa (self, clientes):
        mesa = self.consulta_mesa_livre()
        for cliente in clientes:
            self.mesas[mesa].insert(0, cliente)

    def libera_mesa (self, mesa, clientes):
        for i in range(len(self.mesas[mesa])):
            self.mesas[mesa].pop(-1)
        self.adiciona_cliente_fila_caixa()
        if self.consulta_status_lista_espera() == True:
            self.acomoda_cliente_lista_espera(clientes)

    def consulta_fila_caixa (self):
        for caixa in self.caixas:
            if caixa == []:
                return self.caixas.index(caixa)
        return None

    def adiciona_cliente_fila_caixa (self):
        caixa = self.consulta_fila_caixa()
        if caixa == None:
            if len(self.caixas[0]) <= len(self.caixas[1]):
                self.caixas[0].append('X')
            else:
                self.caixas[1].append('X')
        else:
            self.caixas[caixa].append('X')

    def remove_cliente_fila_caixa (self):
        if self.caixas[0] != []:
            self.caixas[0].pop(0)
        elif self.caixas[1] != []:
            self.caixas[1].pop(0)
        else:
            pass

    def recepciona_cliente (self, clientes):
        if self.consulta_status_lista_espera() == False:
            if self.consulta_mesa_livre() == None:
                self.adiciona_cliente_lista_espera()
            else:
                self.ocupa_mesa(clientes)
        else:
            self.adiciona_cliente_lista_espera()
