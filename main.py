from restaurante import Restaurante
from cliente import Cliente, pessoas
import random, time, os
r = Restaurante()

'''
def imprime2 (t):
    #os.system('clear')
    print('Rodada %s' % t)
    print('Entrada: ', r.entrada.mostrar())
    print('Mesa  1: ', r.mesas[0].mostrar())
    print('Mesa  2: ', r.mesas[1].mostrar())
    print('Mesa  3: ', r.mesas[2].mostrar())
    print('Mesa  4: ', r.mesas[3].mostrar())
    print('Caixa 1: ', r.caixas[0].mostrar())
    print('Caixa 2: ', r.caixas[1].mostrar())
'''

def imprime (t):
    entrada = r.entrada.mostrar()
    mesa1 = r.mesas[0].mostrar()
    mesa2 = r.mesas[1].mostrar()
    mesa3 = r.mesas[2].mostrar()
    mesa4 = r.mesas[3].mostrar()
    caixa1 = r.caixas[0].mostrar()
    caixa2 = r.caixas[1].mostrar()

    print('--------\nRodada {}\n--------\n'.format(t))
    print('Entrada')
    if entrada != []:
        for i in entrada:
            print(i)
    else:
        print('-------')
    print('\n')

    print('{:<30} {:<30} {:<30} {:<30}\n'.format('Mesa 1', 'Mesa 2', 'Mesa 3', 'Mesa 4'))
    for i in range(4):
        print('{:<30} {:<30} {:<30} {:<30}'.format(mesa1[i], mesa2[i], mesa3[i], mesa4[i]))
    print('\n')

    print('Caixa 1')
    if caixa1 != []:
        for i in caixa1:
            print(i[-1])
    else:
        print('-------')
    print('\n')

    print('Caixa 2')
    if caixa2 != []:
        for i in caixa2:
            print(i[-1])
    else:
        print('-------')
    print('\n')

    l = '-'
    for i in range(120):
        l = l + '-'
    print(l,'\n\n')


def main():
    t = 1

    while True:
        i = random.randint(1, 2)
        #time.sleep(r.tempo)

        #cliente chega
        if i == 1:
            #clientes chegaram
            c = Cliente(pessoas())
            #confere se existem clientes na espera
            while (r.entrada.obter_tamanho() > 0): #possui clientes esperando na entrada
                n = 0
                for mesa in r.mesas:
                    if (mesa.verificarSeDesocupada): #caso exista mesa
                        n += 1  
                if (n > 0):
                    #aloca os clientes da fila de entrada em mesas
                    clientes = r.recepcionar_adicionar_clientes_mesa(r.entrada.remover())
            
            clientes = r.recepcionar_adicionar_clientes_mesa(c.clientes)
            
            if (clientes is None):
                imprime(t)
            else:
                r.adicionar_fila_entrada(clientes)
                imprime(t)

        #cliente sai
        elif i == 2:
            for mesa in r.mesas:
                if (mesa.verificarSeOcupada()):
                    clientes = r.remover_clientes_mesa(mesa)
                    r.adicionar_fila_caixa(clientes)
                    imprime(t)
                    break
        
        #cliente paga
        if r.caixas[0].obter_tamanho() > 0 or r.caixas[1].obter_tamanho() > 0:
            r.remover_fila_caixa()
            imprime(t)

        if t == 10:
            break
        t += 1

if __name__ == '__main__':
  main()
