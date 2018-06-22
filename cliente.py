import random

class Cliente:
    def __init__ (self, tempo_preparo):
        self.clientes = [self.quantidade_clientes(), self.tempo_mesa(tempo_preparo)]

    def quantidade_clientes (self):
        return random.randint(1, 4)

    def tempo_mesa (self, tempo_preparo=5):
        return tempo_preparo + random.randint(1, 8)
