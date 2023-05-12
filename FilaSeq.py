class FilaSeq:
    TAM_MAX = 100
    
    def __init__(self):
        self.dados = [0] * FilaSeq.TAM_MAX
        self.inicio = 0
        self.fim = -1
        self.nElementos = 0

    def vazia(self):
        return (self.nElementos == 0)

    def cheia(self):
        return (self.nElementos == FilaSeq.TAM_MAX)

    def tamanho(self):
        return self.nElementos

    def primeiro(self):
        if self.vazia():
            return None
        return self.dados[self.inicio]

    def insere(self, valor):
        if self.cheia():
            return False
        self.fim = (self.fim + 1) % FilaSeq.TAM_MAX  # Circularidade
        self.dados[self.fim] = valor
        self.nElementos += 1
        return True

    def remove(self):
        if self.vazia():
            return None
        valor = self.dados[self.inicio]
        self.inicio = (self.inicio + 1) % FilaSeq.TAM_MAX  # Circularidade
        self.nElementos -= 1
        return valor
