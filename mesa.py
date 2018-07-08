class Mesa (object):
    def __init__ (self, tamanho=4):
        self.cadeiras = [i for i in range(tamanho)]
        self.topo = -1

    # verifica se a pilha esta vazia
    def verificarSeDesocupada(self):
        return (self.topo == -1)

    # verifica se a pilha esta cheia
    def verificarSeOcupada(self):
        return (self.topo != - 1)
    
    # insere um novo elemento na pilha / push
    def ocupar(self, clientes):
        for cliente in clientes:
            self.topo = self.topo + 1
            self.cadeiras[self.topo] = cliente

    # remove o elemento no topo da pilha / pop
    def desocupar(self):
        clientes = []
        while (self.topo != -1):
            clientes.append(self.cadeiras[self.topo])
            self.topo = self.topo - 1
        return clientes
    
    # exibe todos os elementos da pilha
    def mostrar(self):
        t = []
        if (self.verificarSeOcupada()):
            for i in range(self.topo + 1):
                t.append(self.cadeiras[i])
            return t
        return [' ', ' ', ' ', ' ']
