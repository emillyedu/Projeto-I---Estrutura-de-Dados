class No:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.prox = None

    def get_conteudo(self):
        return self.conteudo

    def set_conteudo(self, conteudo):
        self.conteudo = conteudo

    def get_prox(self):
        return self.prox

    def set_prox(self, prox):
        self.prox = prox

class LSE:
    def __init__(self):
        self.cabeca = None
        self.n_elementos = 0

    def vazia(self):
        return self.n_elementos == 0

    def tamanho(self):
        aux = self.cabeca
        cont = 0
        while aux:
            aux = aux.get_prox()
            cont += 1
        return cont

    def elemento(self, pos):
        if self.vazia() or pos < 1 or pos > self.tamanho():
            return None

        aux = self.cabeca
        for i in range(pos - 1):
            aux = aux.get_prox()

        return aux.get_conteudo()

    def posicao(self, dado):
        if self.vazia():
            return None

        aux = self.cabeca
        cont = 1
        while aux:
            if aux.get_conteudo() == dado:
                return cont
            aux = aux.get_prox()
            cont += 1

        return None

    def insere_inicio_lista(self, valor):
        novo_no = No(valor)
        novo_no.set_prox(self.cabeca)
        self.cabeca = novo_no
        self.n_elementos += 1
        return True

    def insere_meio_lista(self, pos, valor):
        novo_no = No(valor)

        aux = self.cabeca
        for i in range(pos - 2):
            aux = aux.get_prox()

        novo_no.set_prox(aux.get_prox())
        aux.set_prox(novo_no)

        self.n_elementos += 1
        return True

    def insere(self, pos, valor):
        if self.vazia() and pos != 1:
            return False

        if pos <= 0 or pos > self.n_elementos + 1:
            return False

        if pos == 1:
            return self.insere_inicio_lista(valor)
        else:
            return self.insere_meio_lista(pos, valor)

    def remove_inicio_lista(self):
        if self.vazia():
            return None

        p = self.cabeca
        valor_removido = p.get_conteudo()

        self.cabeca = p.get_prox()
        self.n_elementos -= 1

        del p

        return valor_removido

    def remove_na_lista(self, pos):
        if self.vazia() or pos < 1 or pos > self.n_elementos:
            return None

        antecessor = None
        atual = self.cabeca
        for i in range(pos - 1):
            antecessor = atual
            atual = atual.get_prox()

        valor_removido = atual.get_conteudo()

        if antecessor:
            antecessor.set_prox(atual.get_prox())
        else:
            self.cabeca = atual.get_prox()

        self.n_elementos -= 1
        del atual

        return valor_removido
    
    def remove(self, pos):
        if self.vazia():
            return None
        
        if pos <= 0 or pos > self.n_elementos:
            return None
        
        if pos == 1:
            return self.remove_inicio_lista()
        else:
            return self.remove_na_lista(pos)
    
