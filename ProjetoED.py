from tkinter import *
from LSE import LSE
from ListaSeq import ListaSeq
from LDE import LDE
from FilaSeq import FilaSeq
from PilhaSeq import PilhaSeq

import tkinter.messagebox as messagebox
import tkinter as tk

def tela1():

    TAM_MAX = 21 # tamanho máximo da lista como definido em listaSeq
    lista = ListaSeq()

    ######################## FUNCOES ###################

    def gerar_view(busca, posicao_busca=None):

        listaview.delete("all")

        square_width = 50
        square_height = 50  
        x_gap = 0
        y_gap = 20
        max_x = 1000
        max_y = 420
        x = x_gap
        y = y_gap

        # Loop para desenhar os quadrados e as setas
        for posicao in range(1, TAM_MAX + 1):
            # Desenha o quadrado

            text_x = x + square_width / 2
            text_y = y + square_height / 2
            max_text_width = square_width - 10

            fill_color = "#4493C7"
            if posicao == posicao_busca  and posicao != None:
                fill_color = "#44C764"

            valor = lista.elemento(posicao)
            if  valor == None:
                fill_color = "#B4EDFC"
            elif valor == busca:  # se o elemento for o buscado alterar a cor da caixa
                fill_color = "#44C764"

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

            valor = lista.elemento(posicao)
            listaview.create_text(text_x, text_y, text=str(valor), width=max_text_width)

            # Verifica se o quadrado chegou ao limite horizontal
            if x + square_width + x_gap > max_x:
                # Passa para a próxima linha
                y = y + square_height + y_gap
                if y > max_y:
                    return KeyError("Lista muito grande")
                x = x_gap
                arrow = listaview.create_line(0, y+square_height/2, x, y+square_height/2)

            else:
                # Move para a direita
                x = x + square_width + x_gap

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")
            caixa1.delete(0, tk.END)
            caixa2.delete(0, tk.END)
            gerar_view(None)
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")

    def remover():
        posicao = int(caixa2.get())
        if lista.remove(posicao) != None:
            print("Removido com sucesso")

            gerar_view(None)
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover, posição inválida")
            
        caixa2.delete(0, tk.END)
    
    def busca_posicao():
        posicao = int(caixa2.get())

        if lista.elemento(posicao) is not None:
            print("Busca feita com sucesso, o valor é: ", lista.elemento(posicao))
            gerar_view(None, posicao)
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")

        caixa2.delete(0, tk.END)

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao_inicial(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao_inicial(valor))
            gerar_view(lista.elemento(lista.posicao_inicial(valor)))
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
            
        caixa1.delete(0, tk.END)

    ######################## INTERFACE GRAFICA (GUI) ###################
    
    label.config(text="Lista Sequencial", bg='#44C7C7')
    root.config(bg='#44C7C7')
    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()

    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg='black')

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:", bg='#44C7C7')

    caixa2 = tk.Entry(root)
    label_caixa2 = tk.Label(root, text="Insira a posição:", bg='#44C7C7')

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12), bg='#44C7C7')
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    caixa2.place(x=300, y=100)
    label_caixa2.place(x=300, y=75)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)
    botao4.place(x=850, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)

    gerar_view(None)

def tela2():

    lista = LSE()

    ######################## FUNCOES ###################

    def gerar_view(busca, posicao_busca=None):

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

            fill_color = "#A884E2"
            if posicao == posicao_busca:
                fill_color = "#4F0DB7"

            valor = lista.elemento(posicao)
            if valor == busca:  # se o elemento for o buscado alterar a cor da caixa
                fill_color = "#4F0DB7"

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

            valor = lista.elemento(posicao)
            listaview.create_text(text_x, text_y, text=str(valor), width=max_text_width)

            arrow = listaview.create_line(x+square_width, y+square_height/2, x+square_width+x_gap, y+square_height/2, arrow=tk.LAST)

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

        #########################################

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")
            caixa1.delete(0, tk.END)
            caixa2.delete(0, tk.END)
            gerar_view(None)
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")

    def remover():
        posicao = int(caixa2.get())
        if lista.remove(posicao) != None:
            print("Removido com sucesso")

            gerar_view(None)
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover, posição inválida")
            
        caixa2.delete(0, tk.END)
    
    def busca_posicao():
        posicao = int(caixa2.get())

        if lista.elemento(posicao) != None:
            print("Busca feita com sucesso, o valor é: ", lista.elemento(posicao))  
            gerar_view(None, posicao)
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")
            
        caixa2.delete(0, tk.END)

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao(valor))
            gerar_view(valor)
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
            
        caixa1.delete(0, tk.END)

    ######################## INTERFACE GRAFICA (GUI) ###################
    label.config(text="LSE", bg='#B68BF9')
    root.config(bg='#B68BF9')
    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()
    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg="black")

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:", bg='#B68BF9')

    caixa2 = tk.Entry(root)
    label_caixa2 = tk.Label(root, text="Insira a posição:", bg='#B68BF9')

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12), bg='#B68BF9')
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    caixa2.place(x=300, y=100)
    label_caixa2.place(x=300, y=75)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)
    botao4.place(x=850, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)

def tela3():
    lista = LDE()
    ######################## FUNCOES ###################

    def gerar_view(busca, posicao_busca=None):

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

            fill_color = "#FFA07A"
            if posicao == posicao_busca:
                fill_color = "#FF4500"

            valor = lista.elemento(posicao)
            if valor == busca:  # se elemento for o buscado alterar a cor do quadrado
                fill_color = "#FF4500"

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

            valor = lista.elemento(posicao)
            listaview.create_text(text_x, text_y, text=str(valor), width=max_text_width)

            arrow = listaview.create_line(x+square_width+x_gap, y+square_height/2, x+square_width, y+square_height/2, arrow='both')

            # Verifica se o quadrado chegou ao limite horizontal
            if x + square_width + x_gap > max_x:
                # Passa para a próxima linha
                y = y + square_height + y_gap
                if y > max_y:
                    return KeyError("Lista muito grande")
                x = x_gap
                arrow = listaview.create_line(0, y+square_height/2, x, y+square_height/2, arrow='both')

            else:
                # Move para a direita
                x = x + square_width + x_gap


    #########################################
        
    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")
            caixa1.delete(0, tk.END)
            caixa2.delete(0, tk.END)
            gerar_view(None)
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")

    def remover():
        posicao = int(caixa2.get())
        if lista.remove(posicao) != None:
            print("Removido com sucesso")
            gerar_view(None)
            caixa2.delete(0, tk.END)
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover, posição inválida")
            caixa2.delete(0, tk.END)

    def busca_posicao():
        posicao = int(caixa2.get())

        if lista.elemento(posicao) != None:
            print("Busca feita com sucesso, o valor é: ", lista.elemento(posicao))
            gerar_view(None, posicao)    
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")
        caixa2.delete(0, tk.END)

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao(valor))
            gerar_view(lista.elemento(lista.posicao(valor)))
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
        caixa1.delete(0, tk.END)


    ######################## INTERFACE GRAFICA (GUI) ###################
    label.config(text="LDE", bg='#FFE4E1')
    root.config(bg='#FFE4E1')
    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()
    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg='black')

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:", bg='#FFE4E1')

    caixa2 = tk.Entry(root)
    label_caixa2 = tk.Label(root, text="Insira a posição:", bg='#FFE4E1')

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12), bg='#FFE4E1')
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    caixa2.place(x=300, y=100)
    label_caixa2.place(x=300, y=75)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)
    botao4.place(x=850, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)

def telaFila():
    
    TAM_MAX = 21 # tamanho máximo da lista como definido em listaSeq
    fila = FilaSeq()

    ######################## FUNCOES ###################

    def gerar_view():

        listaview.delete("all")

        square_width = 50
        square_height = 50  
        x_gap = 0
        y_gap = 20
        max_x = 1000
        max_y = 420
        x = x_gap
        y = y_gap

        # Loop para desenhar os quadrados e as setas
        # Desenha o quadrado

        text_x = x + square_width / 2
        text_y = y + square_height / 2
        max_text_width = square_width - 10

        fill_color = "#4493C7"
        # if posicao == posicao_busca  and posicao != None:
        #     fill_color = "#44C764"

        # valor = fila.elemento(posicao)
        # if  valor == None:
        #     fill_color = "#B4EDFC"
        # elif valor == busca:  # se o elemento for o buscado alterar a cor da caixa
        #     fill_color = "#44C764"

        square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

        valor = fila.primeiro()
        listaview.create_text(text_x, text_y, text=str(valor), width=max_text_width)

        # Verifica se o quadrado chegou ao limite horizontal
        if x + square_width + x_gap > max_x:
            # Passa para a próxima linha
            y = y + square_height + y_gap
            if y > max_y:
                return KeyError("Lista muito grande")
            x = x_gap
            arrow = listaview.create_line(0, y+square_height/2, x, y+square_height/2)

        else:
            # Move para a direita
            x = x + square_width + x_gap

    def inserir():
        valor = int(caixa1.get())
        if fila.insere(valor):
            print("Inserido com sucesso")
            caixa1.delete(0, tk.END)
            gerar_view()
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")

    def remover():
        if fila.remove() != None:
            print("Removido com sucesso")

            gerar_view()
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover")
    
    def primeiro_elemento():

        if fila.primeiro() is not None:
            print("O primeiro elemento é: ", fila.primeiro())
            gerar_view()
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")

    ######################## INTERFACE GRAFICA (GUI) ###################
    
    label.config(text="Fila Sequencial", bg='#44C7C7')
    root.config(bg='#44C7C7')
    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()

    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg='black')

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:", bg='#44C7C7')

    botao1 = tk.Button(root, text="inserir (informe valor)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Exibe primeiro elemento", command= primeiro_elemento, width = 24)
    
    visualizacao = tk.Label(root, text= "Fila: ", font=("Arial", 12), bg='#44C7C7')
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)

    gerar_view(None)

root = tk.Tk()
root.resizable(False, False)
root.geometry("1080x720")
root.title("Projeto Estrutura de Dados")
#root.iconbitmap("ci.ico")
label = tk.Label(root, text="Projeto Estrutura de Dados", font=("Arial", 22, 'bold'), padx=10, pady=10, anchor="center")
label.pack()

def texto_inicial():
    projeto = tk.Label(root, text= "Esse projeto visa demonstrar como as listas sequenciais funcionam.", font=("Arial", 16, 'bold'), padx=5, pady=5, anchor="w")
    instrucoes = tk.Label(root, text= "Algumas instruções sobre o programa: ", font=("Arial", 16), padx=5, pady=5, anchor="w")
    instrucao1 = tk.Label(root, text= "Ao trocar de tela (de LSE para LDE, por exemplo), sua lista será excluída.", font=("Arial", 16), padx=5, pady=5, anchor="w")
    projeto.pack()
    instrucoes.pack()
    instrucao1.pack()

def botoes_iniciais():
    # Botão para trocar para tela 1
    botao1 = tk.Button(root, text="Lista Sequencial", command=tela1, width = 12)
    botao1.place(x=0, y=27)

    # Botão para trocar para tela 2
    botao2 = tk.Button(root, text="LSE", command=tela2, width = 12)
    botao2.place(x=0, y=53)

    # Botão para trocar para tela 3
    botao3 = tk.Button(root, text="LDE", command=tela3, width = 12)
    botao3.place(x=0, y=79)
    
    # Botão para trocar para tela Fila
    botao3 = tk.Button(root, text="Fila Sequencial", command=telaFila, width = 12)
    botao3.place(x=0, y=106)
    
texto_inicial()
botoes_iniciais()

root.mainloop()