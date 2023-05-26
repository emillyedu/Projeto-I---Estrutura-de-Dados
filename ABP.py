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

    def in_ordem(self, T):
        if T is not None:
            self.in_ordem(T.left)
            print(T.value, end=" ")
            self.in_ordem(T.right)

    def exibe_in_ordem(self):
        if self.raiz is None:
            print("Arvore vazia")
        else:
            self.in_ordem(self.raiz)

    def pre_ordem(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.pre_ordem(node.left)
            self.pre_ordem(node.right)

    def exibe_pre_ordem(self):
        if self.raiz is None:
            print("Arvore vazia")
        else:
            self.pre_ordem(self.raiz)

    def pos_ordem(self, node):
        if node is not None:
            self.pos_ordem(node.left)
            self.pos_ordem(node.right)
            print(node.value, end=" ")

    def exibe_pos_ordem(self):
        if self.raiz is None:
            print("Arvore vazia")
        else:
            self.pos_ordem(self.raiz)

    def insere(self, valor):
        novo_no = Node(valor)
        novo_no.left = None
        novo_no.right = None

        if self.raiz is None:
            self.raiz = novo_no
            return True

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
    

    # Percurso em ordem (in-order) na árvore
    def e_in_ordem(self, T, nodes):
        if T is not None:
            self.e_in_ordem(T.left, nodes)
            nodes.append(T.value)
            self.e_in_ordem(T.right, nodes)

    # Percurso em pré-ordem (pre-order) na árvore
    def e_pre_ordem(self, T, nodes):
        if T is not None:
            nodes.append(T.value)
            self.e_pre_ordem(T.left, nodes)
            self.e_pre_ordem(T.right, nodes)

    # Percurso em pós-ordem (post-order) na árvore
    def e_pos_ordem(self, T, nodes):
        if T is not None:
            self.e_pos_ordem(T.left, nodes)
            self.e_pos_ordem(T.right, nodes)
            nodes.append(T.value)