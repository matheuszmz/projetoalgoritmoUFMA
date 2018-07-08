class Fila (object):
	def __init__(self, tamanho=10):
		self.vetor = [i for i in range(10)]
		self.fim = -1

	def verificarVazia (self):
		return (self.fim == -1)

	# insere um novo elemento no final da fila / enqueue
	def adicionar(self, clientes):
		self.fim += 1
		self.vetor[self.fim] = clientes

	# remove o elemento no inicio da fila / dequeue
	def remover(self):
		temp = self.vetor[0]
		del self.vetor[0]
		self.fim -= 1
		return temp
	
	# retorna o numero de elementos na fila
	def	obter_tamanho(self):
		t = 0
		for i in range(self.fim + 1):
			t += 1
		return t

	# exibe todos os elementos da fila
	def mostrar(self):
		t = []
		for i in range(self.fim + 1):
			if (self.vetor[i] is not None):
				t.append(self.vetor[i])
		return t
