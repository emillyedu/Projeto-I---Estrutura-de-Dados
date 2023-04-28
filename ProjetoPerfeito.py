from tkinter import *
from LSE import LSE
from ListaSeq import ListaSeq
from LDE import LDE

import tkinter.messagebox as messagebox
import tkinter as tk

def tela1():

    lista = ListaSeq()

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

            fill_color = "blue"
            if posicao == posicao_busca:
                fill_color = "green"

            valor = lista.elemento(posicao)
            if valor == busca:  # if element matches the search value, set fill color to green
                fill_color = "green"

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

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


        #########################################

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")    
            gerar_view(None)
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")
            
        caixa1.delete(0, tk.END)
        caixa2.delete(0, tk.END)

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
            messagebox.showinfo(message=("Busca feita com sucesso, o valor é: ", lista.elemento(posicao)))
            gerar_view(None, posicao)
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")

        caixa2.delete(0, tk.END)

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao_inicial(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao_inicial(valor))
            messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.posicao_inicial(valor)))
            gerar_view(lista.elemento(lista.posicao_inicial(valor)))
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
            
        caixa1.delete(0, tk.END)

    ######################## INTERFACE GRAFICA (GUI) ###################
    label.config(text="LSE")

    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()
    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg='black')

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:")

    caixa2 = tk.Entry(root)
    label_caixa2 = tk.Label(root, text="Insira a posição:")

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12))
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    caixa2.place(x=300, y=86)
    label_caixa2.place(x=300, y=65)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)
    botao4.place(x=850, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)
    #listaview.pack('bottom')

def tela2():

    lista = LSE()

    ######################## FUNCOES ###################

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

            arrow = listaview.create_line(x+square_width, y+square_height/2, x+square_width+x_gap, y+square_height/2, arrow=tk.LAST)
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

        #########################################

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")    
            gerar_view(None)
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")
            
        caixa1.delete(0, tk.END)
        caixa2.delete(0, tk.END)

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
            messagebox.showinfo(message=("Busca feita com sucesso, o valor é: ", lista.elemento(posicao)))
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posição")
            
        caixa2.delete(0, tk.END)

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao(valor))
            messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.posicao(valor)))
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
            
        caixa1.delete(0, tk.END)

    ######################## INTERFACE GRAFICA (GUI) ###################
    label.config(text="LSE")

    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()

    botoes_iniciais()
    ######################## COMPONENTES (WIDGETS) ###################
    
    linha = tk.Frame(root, width=1080, height=1, bg='black')

    caixa1 = tk.Entry(root)
    label_caixa1 = tk.Label(root, text="Insira o valor:")

    caixa2 = tk.Entry(root)
    label_caixa2 = tk.Label(root, text="Insira a posição:")

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12))
    listaview = tk.Canvas(root, width= 1080, height= 490, bg= "white")

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################

    linha.place(x=0, y=240)

    caixa1.place(x=300, y=43)
    label_caixa1.place(x=300, y=20)

    caixa2.place(x=300, y=86)
    label_caixa2.place(x=300, y=65)

    botao1.place(x=550, y=43)
    botao2.place(x=850, y=43)
    botao3.place(x=550, y=80)
    botao4.place(x=850, y=80)

    visualizacao.place(x= 360, y=230)
    listaview.place(x= 0, y= 250)
    #listaview.pack('bottom')


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
            if valor == busca:  # if element matches the search value, set fill color
                fill_color = "#FF4500"

            square = listaview.create_rectangle(x, y, x+square_width, y+square_height, fill=fill_color)

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

    def busca_valor():
        valor = int(caixa1.get())

        if lista.posicao(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao(valor))
            messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.posicao(valor)))
            gerar_view(lista.elemento(lista.posicao_inicial(valor)))
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao buscar pelo valor")
        caixa2.delete(0, tk.END)

    def busca_posicao():
        posicao = int(caixa2.get())

        if lista.elemento(posicao) != None:
            messagebox.showinfo(message=("Busca feita com sucesso, o valor é: ", lista.elemento(posicao)))
            gerar_view(None, posicao)    
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar por posicao")
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
    #listaview.pack('bottom')


root = tk.Tk()
root.resizable(False, False)
root.geometry("1080x720")
root.title("Projeto Estrutura de Dados")

# Label para exibir a tela atual
label = tk.Label(root, text="Projeto Estrutura de Dados")
label.pack()

def texto_inicial():
    projeto = tk.Label(root, text= "Esse projeto visa demonstrar como as listas sequenciais funcionam.", font=("Arial", 12))
    instrucoes = tk.Label(root, text= "Algumas instruções sobre o programa: ", font=("Arial", 12))
    instrucao1 = tk.Label(root, text= "Ao trocar de tela (de LSE para LDE, por exemplo), sua lista será excluída.", font=("Arial", 12))
    projeto.pack()
    instrucoes.pack()
    instrucao1.pack()

def botoes_iniciais():
    # Botão para trocar para tela 1
    botao1 = tk.Button(root, text="Lista Sequencial", command=tela1, width = 12)
    botao1.place(x=0, y=26)

    # Botão para trocar para tela 2
    botao2 = tk.Button(root, text="LSE", command=tela2, width = 12)
    botao2.place(x=0, y=53)

    # Botão para trocar para tela 3
    botao3 = tk.Button(root, text="LDE", command=tela3, width = 12)
    botao3.place(x=0, y=79)
    
texto_inicial()
botoes_iniciais()

root.mainloop()