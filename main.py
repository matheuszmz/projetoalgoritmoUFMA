from restaurante import Restaurante
from cliente import Cliente
import random, time

n = 1
r = Restaurante()


def imprime ():
    print('Lista de espera: ', r.lista_espera)
    print('Mesas: ', r.mesas)
    print('Caixas: ', r.caixas)

while True:
    n = n + 1
    i = random.randint(1, 3)
    time.sleep(2)
    c = Cliente(r.tempo_preparo)
    clientes = c.clientes

    #cliente chega
    if i == 1:
        r.recepciona_cliente(clientes)
        imprime()
    #cliente sai
    elif i == 2:
        mesa = r.consulta_mesa_ocupada()
        if mesa != None:
            r.libera_mesa(mesa, clientes)
            imprime()
    #cliente paga
    elif i == 3:
        r.remove_cliente_fila_caixa()
        imprime()

    if n == 20:
        break
