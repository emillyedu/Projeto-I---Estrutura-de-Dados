class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ABP:
    def __init__(self):
        self.raiz = None

    def vazia(self):
        return self.raiz is None

    def busca(self, T, valor):
        if T is None:
            return None

        if T.value == valor:
            return T

        if valor < T.value:
            return self.busca(T.left, valor)
        else:
            return self.busca(T.right, valor)

    def busca_recursiva(self, valor):
        return self.busca(self.raiz, valor)

    def busca_iterativa(self, valor):
        if self.vazia():
            return None

        aux = self.raiz
        while aux is not None:
            if aux.value == valor:
                return aux

            if valor < aux.value:
                aux = aux.left
            else:
                aux = aux.right

        return None

    def insere(self, valor):
        novo_no = Node(valor)
        novo_no.left = None
        novo_no.right = None

        if self.raiz is None:
            self.raiz = novo_no
            return True

        # Verificar altura da árvore
        altura = self.altura_arvore(self.raiz)
        if altura > 4:
            print("Distância máxima entre a raiz e o nó mais baixo excedida")
            return False

        aux = self.raiz
        p = None
        while aux is not None:
            p = aux

            if valor == aux.value:
                return False

            if valor < aux.value:
                aux = aux.left
            else:
                aux = aux.right

        if valor < p.value:
            p.left = novo_no
        else:
            p.right = novo_no

        return True

    def altura_arvore(self, node):
        if node is None:
            return 0

        altura_esq = self.altura_arvore(node.left)
        altura_dir = self.altura_arvore(node.right)
        return max(altura_esq, altura_dir) + 1
    

    # Percurso em ordem (in-order) na árvore para ilustração
    def gerar_in_ordem(self, T, nodes):
        if T is not None:
            self.gerar_in_ordem(T.left, nodes)
            nodes.append(T.value)
            self.gerar_in_ordem(T.right, nodes)

    # Percurso em pré-ordem (pre-order) na árvore para ilustração
    def gerar_pre_ordem(self, T, nodes):
        if T is not None:
            nodes.append(T.value)
            self.gerar_pre_ordem(T.left, nodes)
            self.gerar_pre_ordem(T.right, nodes)

    # Percurso em pós-ordem (post-order) na árvore para ilustração
    def gerar_pos_ordem(self, T, nodes):
        if T is not None:
            self.gerar_pos_ordem(T.left, nodes)
            self.gerar_pos_ordem(T.right, nodes)
            nodes.append(T.value)
