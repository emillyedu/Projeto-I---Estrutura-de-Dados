from tkinter import *
from LSE import LSE
from ListaSeq import ListaSeq
from LDE import LDE

import tkinter.messagebox as messagebox
import tkinter as tk

elemento = 0 
lista_LDE = LDE()

def tela1():

    lista = ListaSeq()

    ######################## FUNCOES ###################

    def gerar_view():

        listaview.delete("all")
        
        for posicao in range(1, lista.tamanho()+1):
            valor = lista.elemento(posicao)
            x = 200 + posicao*50
            y = 240
            inserir = "- [" + str(valor) + "] -"
            listaview.create_text(x, y, text=inserir, font=("Arial", 12))

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")    
            gerar_view()
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")
            
        caixa1.delete(0, tk.END)
        caixa2.delete(0, tk.END)

    def remover():
        posicao = int(caixa2.get())
        if lista.remove(posicao) != None:
            print("Removido com sucesso")

            gerar_view()
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover, posição inválida")
            
        caixa2.delete(0, tk.END)
    
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

    ######################## INTERFACE GRAFICA (GUI) ###################
    label.config(text="Lista Sequencial")

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
    listaview = tk.Canvas(root, width= 1080, height= 480, bg= "white")

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

    def gerar_view():

        listaview.delete("all")
        
        for posicao in range(1, lista.tamanho()+1):
            valor = lista.elemento(posicao)
            x = 200 + posicao*50
            y = 240
            inserir = "  [" + str(valor) + "]   =>"
            listaview.create_text(x, y, text=inserir, font=("Arial", 12))

    def inserir():
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista.insere(posicao, valor):
            print("Inserido com sucesso")    
            gerar_view()
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")
            
        caixa1.delete(0, tk.END)
        caixa2.delete(0, tk.END)

    def remover():
        posicao = int(caixa2.get())
        if lista.remove(posicao) != None:
            print("Removido com sucesso")

            gerar_view()
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover, posição inválida")
            
        caixa2.delete(0, tk.END)
    
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

        if lista.posicao(valor) != None:
            print("Busca feita com sucesso, a posição é: ", lista.posicao(valor))
            messagebox.showinfo(message=("Busca feita com sucesso, a posição é: ", lista.posicao(valor)))
            
        else:
            print("Erro ao buscar, valor nao esta na lista ou é inválido")
            messagebox.showerror("Erro", "Erro ao bucar valor")
            
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
    listaview = tk.Canvas(root, width= 1080, height= 480, bg= "white")

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
    global lista_LDE

    ######################## FUNCOES ###################
    def gerar_view():
        listaview.delete("all")
        
        for posicao in range(1, lista_LDE.tamanho()+1):
            valor = lista_LDE.elemento(posicao)
            x = 200 + posicao*50
            y = 240
            inserir = "<=   [" + str(valor) + "]   =>"
            listaview.create_text(x, y, text=inserir, font=("Arial", 12))
        
    def inserir_LDE():
        global elemento
        valor = int(caixa1.get())
        posicao = int(caixa2.get())
        if lista_LDE.insere(posicao, valor):
            print("Inserido com sucesso")
            caixa1.delete(0, tk.END)
            caixa2.delete(0, tk.END)
            elemento=elemento+1
            gerar_view()
        else:
            print("Erro ao inserir")
            messagebox.showerror("Erro", "Erro ao inserir")

    def remover_LDE():
        global elemento
        posicao = int(caixa2.get())
        if posicao > elemento:
            print("Não existe na lista_LDE")
            messagebox.showerror("Erro", "Nessa posição não há valor")
            caixa2.delete(0, tk.END)
        elif lista_LDE.remove(posicao) > 0:
            print("Removido com sucesso")
            
            caixa2.delete(0, tk.END)
            elemento=elemento-1
            gerar_view()
        else:
            print("Erro ao remover")
            messagebox.showerror("Erro", "Erro ao remover")
    
    def busca_valor_LDE():
        global elemento
        posicao = int(caixa2.get())

        if posicao > elemento:
            print("Não existe na lista_LDE")
            messagebox.showerror("Erro", "Não existe essa posição na lista_LDE")
        elif lista_LDE.elemento(posicao) > 0:
            print("Busca feita com sucesso, o valor é: ", lista_LDE.elemento(posicao))
            messagebox.showerror("Busca feita com sucesso!", "O valor é: ", lista_LDE.elemento(posicao))
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar")
        caixa2.delete(0, tk.END)

    def busca_posicao_LDE():
        global elemento
        valor = int(caixa1.get())

        if valor > elemento:
            print("Não existe na lista_LDE")
            messagebox.showerror("Erro", "Não existe esse valor na lista_LDE")
        elif lista_LDE.posicao(valor) > 0:
            print("Busca feita com sucesso, a posicao é: ", lista_LDE.posicao(valor))
            messagebox.showerror("Busca feita com sucesso!", "A posicao é: ", lista_LDE.posicao(valor))
        else:
            print("Erro ao buscar")
            messagebox.showerror("Erro", "Erro ao buscar")
        caixa1.delete(0, tk.END)

    ######################## INTERFACE GRAFICA (GUI) ###################
    
    label.config(text="LDE")
    # Removendo os widgets da tela anterior, se existirem
    for widget in root.winfo_children():
        if widget != label:
            widget.destroy()
    linha = tk.Frame(root, width=1080, height=1, bg='black')
    linha.place(x=0, y=240)

    botoes_iniciais()

    ######################## POSICAO DOS COMPONENTES (LAYOUT) ###################   
    # Criando as caixas de texto
    caixa1 = tk.Entry(root)
    caixa1.place(x=150, y=43)
    label_caixa1 = tk.Label(root, text="Insira o valor:")
    label_caixa1.place(x=150, y=20)

    caixa2 = tk.Entry(root)
    caixa2.place(x=150, y=86)
    label_caixa2 = tk.Label(root, text="Insira a posição:")
    label_caixa2.place(x=150, y=63)

    botao1 = tk.Button(root, text="inserir (informe val e pos)", command=inserir_LDE, width= 24)
    botao2 = tk.Button(root, text="Remover (informe posicao)", command= remover_LDE, width = 24)
    botao3 = tk.Button(root, text="Busca Posição (informe valor)", command= busca_valor_LDE, width = 24)
    botao4 = tk.Button(root, text="Busca Valor (informe posicao)", command= busca_posicao_LDE, width = 24)
    
    visualizacao = tk.Label(root, text= "Lista: ", font=("Arial", 12))
    listaview = tk.Canvas(root, width= 1080, height= 480, bg= "white")

    ######################## COMPONENTES (WIDGETS) ###################
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