import random

class Cliente:
    def __init__ (self, tempo_preparo):
        self.clientes = self.quantidade_clientes()

    def quantidade_clientes (self):
        cs = random.randint(1, 4)
        clientes = []
        for c in range(cs):
            clientes.append('X')
        return clientes
