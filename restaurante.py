#quatro pilhas as mesas
#tres filas caixas e fila de entrada
from fila import Fila
from mesa import Mesa

class Restaurante:
    def __init__ (self):
        self.entrada = Fila()
        self.mesas = [Mesa(), Mesa(), Mesa(), Mesa()]
        self.caixas = [Fila(), Fila()]
        self.tempo = 2
    
    def localiza_mesa_disponivel (self):
        for mesa in self.mesas:
            if (mesa.verificarSeDesocupada()):
                return mesa
        return

    def recepcionar_adicionar_clientes_mesa (self, clientes):
        for mesa in self.mesas:
            if (mesa.verificarSeDesocupada()):
                mesa.ocupar(clientes)
                return
        return clientes
    
    def remover_clientes_mesa (self, mesa):
        clientes = mesa.desocupar()
        self.adicionar_fila_caixa(clientes)

    def adicionar_fila_caixa (self, clientes):
        if self.caixas[0].obter_tamanho() <= self.caixas[1].obter_tamanho():
            self.caixas[0].adicionar(clientes)
        else:
            self.caixas[1].adicionar(clientes)
    
    def remover_fila_caixa (self):
        if (self.caixas[0].fim != -1):
            return self.caixas[0].remover()
        elif (self.caixas[1].fim != -1):
            return self.caixas[1].remover()
        else:
            return

    def adicionar_fila_entrada (self, clientes):
        self.entrada.adicionar(clientes)
    
    def remover_fila_entrada (self):
        return self.entrada.remover()
