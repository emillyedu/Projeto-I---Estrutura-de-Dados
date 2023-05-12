class PilhaSeq:
    TAM_MAX = 100

    def __init__(self):
        self.dados = [0] * PilhaSeq.TAM_MAX
        self.topo = -1

    def vazia(self):
        return self.topo == -1

    def cheia(self):
        return self.topo == PilhaSeq.TAM_MAX - 1

    def tamanho(self):
        return self.topo + 1

    def top(self):
        if self.vazia():
            return -1
        return self.dados[self.topo]

    def push(self, valor):
        if self.cheia():
            return False
        self.topo += 1
        self.dados[self.topo] = valor
        return True

    def pop(self):
        if self.vazia():
            return -1
        valor = self.dados[self.topo]
        self.topo -= 1
        return valor
