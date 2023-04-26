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



def gerar_view(busca):

        listaview.delete("all")
        
        square_width = 50
        square_height = 50  
        x_gap = 50
        y_gap = 20
        max_x = 1000
        max_y = 420
        x = x_gap
        y = y_gap

        # Loop para desenhar os quadrados e as setas
        for posicao in range(1, lista.tamanho() + 1):
            # Desenha o quadrado

            text_x = x + square_width / 2
            text_y = y + square_height / 2
            max_text_width = square_width - 10

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill="blue")

            valor = lista.elemento(posicao)
            listaview.create_text(text_x, text_y, text=str(valor), width=max_text_width)

            arrow = listaview.create_line(x+square_width, y+square_height/2, x+square_width+x_gap, y+square_height/2)
            #arrow = listaview.create_line(x+square_width+x_gap, y+square_height/2, x+square_width, y+square_height/2, arrow=tk.LAST)

            # Verifica se o quadrado chegou ao limite horizontal
            if x + square_width + x_gap > max_x:
                # Passa para a próxima linha
                y = y + square_height + y_gap
                if y > max_y:
                    return KeyError("Lista muito grande")
                x = x_gap
                arrow = listaview.create_line(0, y+square_height/2, x, y+square_height/2, arrow=tk.LAST)

            else:
                # Move para a direita
                x = x + square_width + x_gap


def busca_posicao():
    posicao = int(caixa2.get())

    if lista.elemento(posicao) != None:
        print("Busca feita com sucesso, o valor é: ", lista.elemento(posicao))
        messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.elemento(posicao)))        
    else:
        print("Erro ao buscar")
        messagebox.showerror("Erro", "Erro ao bucar posição")
        
    caixa2.delete(0, tk.END)

def busca_valor():
    valor = int(caixa1.get())

    if lista.posicao_inicial(valor) != None:
        print("Busca feita com sucesso, a posição é: ", lista.posicao_inicial(valor))
        messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.posicao_inicial(valor)))
        
    else:
        print("Erro ao buscar, valor nao esta na lista ou é inválido")
        messagebox.showerror("Erro", "Erro ao bucar valor")
        
    caixa1.delete(0, tk.END)