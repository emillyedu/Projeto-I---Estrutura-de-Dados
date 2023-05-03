class ListaSeq:

    TAM_MAX = 10

    def __init__(self):
        self.dados = [0] * ListaSeq.TAM_MAX
        self.nElementos = 0

    def vazia(self):
        return self.nElementos == 0

    def cheia(self):
        return self.nElementos == ListaSeq.TAM_MAX

    def tamanho(self):
        return self.nElementos

    def elemento(self, pos):
        if pos > self.nElementos or pos <= 0:
            return None
        return self.dados[pos-1]

    def posicao_inicial(self, valor):
        for i in range(self.nElementos):
            if self.dados[i] == valor:
                return i+1
        return None

    def posicao_desloc(self, valor, desloc):
        for i in range(desloc, self.nElementos):
            if self.dados[i] == valor:
                return i+1
        return None

    def insere(self, pos, valor):
        if self.cheia() or pos > self.nElementos+1 or pos <= 0:
            return False
        for i in range(self.nElementos, pos-1, -1):
            self.dados[i] = self.dados[i-1]
        self.dados[pos-1] = valor
        self.nElementos += 1
        return True

    def remove(self, pos):
        if pos > self.nElementos or pos < 1:
            return None
        aux = self.dados[pos-1]
        for i in range(pos-1, self.nElementos-1):
            self.dados[i] = self.dados[i+1]
        self.nElementos -= 1
        return aux
