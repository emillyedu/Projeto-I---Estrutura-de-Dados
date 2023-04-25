from LDE import LDE

minhaLista = LDE()

if minhaLista.vazia():
    print("Lista inicialmente vazia!")
else:
    print("Lista criada não estava vazia!")

minhaLista.insere(1, 10)
minhaLista.insere(2, 20)
minhaLista.insere(3, 30)
minhaLista.insere(4, 40)

minhaLista.insere(3, 25)
minhaLista.insere(5, 35)

print("\nLista após as primeiras inserções:")
for i in range(1, minhaLista.tamanho() + 1):
    dado = minhaLista.elemento(i)
    print(f"{i}-ésimo elemento da lista = {dado}")

minhaLista.insere(2, 2000)
ret = minhaLista.insere(1, 101)
print(f"Inserção do 101 na posição 1 = {ret}")

print("\nLista após o segundo grupo de inserções:")
for i in range(1, minhaLista.tamanho() + 1):
    dado = minhaLista.elemento(i)
    print(f"{i}-ésimo elemento da lista = {dado}")

ret = minhaLista.insere(20, 500)
print(f"Inserção do 500 na posição 20 = {ret}")

print("Posição do elemento 10 =", minhaLista.posicao(10))
print("Posição do elemento 30 =", minhaLista.posicao(30))
print("Posição do elemento 40 =", minhaLista.posicao(40))
print("Posição do elemento 15 =", minhaLista.posicao(15))

print("Tamanho =", minhaLista.tamanho())

dado = minhaLista.remove(3)
print("\nDado removido =", dado, "\n")

print("Lista depois da primeira remoção:")
for i in range(1, minhaLista.tamanho() + 1):
    dado = minhaLista.elemento(i)
    print(f"{i}-ésimo elemento da lista = {dado}")

dado = minhaLista.remove(6)
print("\nDado removido =", dado, "\n")

print("Lista depois da segunda remoção:")
for i in range(1, minhaLista.tamanho() + 1):
    dado = minhaLista.elemento(i)
    print(f"{i}-ésimo elemento da lista = {dado}")
