class No:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.prox = None
        self.ant = None

    def get_conteudo(self):
        return self.conteudo

    def set_conteudo(self, novo_conteudo):
        self.conteudo = novo_conteudo

    def get_prox(self):
        return self.prox

    def set_prox(self, novo_prox):
        self.prox = novo_prox

    def get_ant(self):
        return self.ant

    def set_ant(self, novo_ant):
        self.ant = novo_ant

class LDE:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.nElementos = 0

    def vazia(self):
        if self.nElementos == 0:
            return True
        else:
            return False

    def tamanho(self):
        return self.nElementos

    def elemento(self, pos):
        aux = self.inicio
        cont = 1

        if self.vazia():
            return -1

        if (pos < 1) or (pos > self.tamanho()):
            return -1

        while cont < pos:
            aux = aux.get_prox()
            cont += 1

        return aux.get_conteudo()

    def posicao(self, dado):
        cont = 1
        aux = self.inicio

        if self.vazia():
            return -1

        while aux != None:
            if aux.get_conteudo() == dado:
                return cont
            aux = aux.get_prox()
            cont += 1

        return -1

    def insere_inicio_lista(self, valor):
        novo_no = No(valor)

        novo_no.set_prox(self.inicio)
        novo_no.set_ant(None)

        if self.vazia():
            self.fim = novo_no
        else:
            self.inicio.set_ant(novo_no)

        self.inicio = novo_no
        self.nElementos += 1
        return True

    def insere_meio_lista(self, pos, dado):
        cont = 1
        novo_no = No(dado)
        aux = self.inicio

        while cont < pos - 1 and aux != None:
            aux = aux.get_prox()
            cont += 1

        if aux == None:
            return False

        novo_no.set_ant(aux)
        novo_no.set_prox(aux.get_prox())
        aux.get_prox().set_ant(novo_no)
        aux.set_prox(novo_no)

        self.nElementos += 1
        return True

    def insere_fim_lista(self, dado):
        novo_no = No(dado)
        novo_no.set_ant(self.fim)
        novo_no.set_prox(None)

        self.fim.set_prox(novo_no)
        self.fim = novo_no

        self.nElementos += 1
        return True

    def insere(self, pos, dado):
        if self.vazia() and pos != 1:
            return False

        if pos == 1:
            return self.insere_inicio_lista(dado)
        elif pos == self.nElementos + 1:
            return self.insere_fim_lista(dado)
        else:
            return self.insere_meio_lista(pos, dado)
    
    def removeInicioListaUnitaria(self):
        dado = self.inicio.getConteudo()
        
        del self.inicio
        
        self.inicio = None
        self.fim = None
        self.nElementos -= 1
        
        return dado

    def removeInicioLista(self):
        if self.inicio is None:  # verifica se a lista está vazia
            return None

        p = self.inicio
        dado = p.conteudo  # obtém o conteúdo do nó removido

        self.inicio = p.prox  # retira o primeiro elemento da lista

        if self.inicio is not None:  # verifica se ainda há elementos na lista
            self.inicio.ant = None  # atualiza o ponteiro 'ant' do novo início

        self.nElementos -= 1

        del p  # libera a memória do nó removido

        return dado
    
    def removeMeioLista(self, pos):
        p = self.inicio
        n = 1

        # Localiza o nó que será removido
        while n <= pos-1 and p is not None:
            p = p.get_prox()
            n += 1

        if p is None:
            return -1  # pos. inválida

        dado = p.get_conteudo()
        p.get_ant().set_prox(p.get_prox())
        p.get_prox().set_ant(p.get_ant())

        self.nElementos -= 1

        # Libera a memoria da regiao apontada por p
        del p

        return dado

    def removeFimLista(self):
        if self.nElementos == 0:
            return None

        p = self.fim
        dado = p.get_conteudo()

        if self.nElementos == 1:
            self.inicio = None
            self.fim = None
        else:
            self.fim.get_ant().set_prox(None)
            self.fim = self.fim.get_ant()

        self.nElementos -= 1

        del p

        return dado
    
    def remove(self, pos):
        # Lista vazia
        if self.vazia():
            return -1
        
        # Remoção do elemento da cabeça da lista
        if pos == 1 and self.tamanho() == 1:
            return self.removeInicioListaUnitaria()
        elif pos == 1:
            return self.removeInicioLista()
        # Remocao no fim da lista
        elif pos == self.tamanho():
            return self.removeFimLista()
        # Remoção em outro lugar da lista
        else:
            return self.removeMeioLista(pos)

    def get_elementos(self):
        elementos = []
        current = self.inicio
        while current is not None:
            elementos.append(current.get_conteudo())
            current = current.get_prox()
        return elementos