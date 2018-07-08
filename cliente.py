# -*- coding: utf-8 -*-
import random

def pessoas():
    nomes = ['Joao', 'Jose', 'Felipe', 'Mateus', 'Gustavo', 'Ezequias',
    'Lucas', 'Tiago', 'Manoel', 'Francisco', 'Hugo', 'Miguel']
    sobrenomes = ['Andrade', 'Silva', 'Santana', 'Oliveira', 'Correia',
    'Costa', 'Carvalho', 'Leal', 'Souza', 'Fernandes', 'Sampaio', 'Camargo']
    #cs = random.randint(1, 4)
    cs = 4
    clientes = []
    for c in range(cs):
        clientes.append('{} {}'.format(
            nomes[random.randint(0, 11)],
            sobrenomes[random.randint(0, 11)]
            ))
    return clientes

class Cliente:
    def __init__ (self, clientes):
        self.clientes = clientes
