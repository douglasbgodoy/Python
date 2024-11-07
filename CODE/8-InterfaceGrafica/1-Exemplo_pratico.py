""" 
 * Nome: Exemplos de Interface Grafica
 * Descrição: Ao final da aula, os alunos serão capazes de usar Interface Grafica.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-10-10
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""
# Programa 13.1: Um primeiro programa com tkinter

import tkinter as tk 
from tkinter import ttk

raiz = tk. Tk()
raiz.title("Primeira Janela")
raiz.geometry("250x50")
quadro = ttk.Frame(raiz)

texto = ttk.Label(quadro, text="Olá GUI!") 
texto.pack()

botão = ttk.Button(quadro, text="Sai", command=raiz.destroy) 
botão.pack() 
quadro.pack(expand=True) 
raiz.mainloop()



#Programa 13.2: Contando cliques

import tkinter as tk 
from tkinter import ttk

contador_1 = 0
contador_2 = 0

def formata_contador (contador, valor):
    return f"Contador {contador}: {valor}"

def conta_1():
    global contador_1, l_contador_1
    contador_1 += 1
    l_contador_1["text"] = formata_contador(1, contador_1)

def conta_2():
    global contador_2, l_contador_2
    contador_2 += 1
    l_contador_2["text"] = formata_contador(2, contador_2)

raiz = tk. Tk()
raiz.title("Contadores") 
raiz.geometry("250x100")

quadro = ttk. Frame(raiz)

l_contador_1 = ttk.Label(quadro, text=formata_contador(1, contador_1))
l_contador_1.pack()
botao_1 = ttk.Button(quadro, text="Adiciona ao contador 1", command=conta_1)
botao_1.pack()
l_contador_2 = ttk.Label(quadro, text=formata_contador (2, contador_2))
l_contador_2.pack()
botao_2 = ttk.Button(quadro, text="Adiciona ao contador 2", command=conta_2)
botao_2.pack()
quadro.pack(expand=True)
raiz.mainloop()


# Programa 13.3: Usando classes para compor a interface
import tkinter as tk 
from tkinter import ttk

class Aplicação (tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador_1 = 0
        self.contador_2 = 0
        self.title("Contadores") 
        self.geometry("250x100")
        self.cria_quadro()

    def cria_quadro(self):
        self.quadro = ttk.Frame(self)
        self.l_contador_1 = ttk.Label(self.quadro, text=self.formata_contador (1, self.contador_1))
        self.l_contador_1.pack()
        self.botao_1 = ttk.Button(self.quadro, text="Adiciona ao contador 1", command=self .conta_1)
        self.botao_1.pack()
        self.l_contador_2 = ttk.Label(self.quadro, text=self.formata_contador (2, self.contador_2))
        self.l_contador_2.pack()
        self.botao_2 = ttk.Button (self.quadro, text="Adiciona ao contador 2", command=self. conta_2)
        self.botao_2.pack()
        self.quadro.pack(expand=True)

    def formata_contador (self, contador, valor): 
        return f"Contador {contador}: {valor}"

    def conta_1(self):
        self.contador_1 += 1
        self.l_contador_1["text"] = self.formata_contador(1, self.contador_1)

    def conta_2(self):
        self.contador_2 += 1
        self.l_contador_2["text"] = self.formata_contador(2, self.contador_2)

raiz = Aplicação() 
raiz.mainloop()



# Programa 13.4: Adicionando contadores
import tkinter as tk 
from tkinter import ttk

class Contador (ttk.Frame): 
    def __init__ (self, numero, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contador = 0
        self.numero = numero
        self.label = ttk.Label(self,text=self. formata_contador (self.numero, self.contador))
        self.label.pack()
        self.botao = ttk.Button(self, text=f"Adiciona ao contador {self.numero}", command=self.conta)
        self.botao.pack()
        self.pack()

    def formata_contador (self, contador, valor): 
        return f"Contador {contador}: {valor}"

    def conta(self):
        self.contador += 1
        self.label["text"] = self. formata_contador (self.numero, self. contador)

class Aplicação(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contadores = []
        self.cria_quadro()
    def cria_quadro(self):
        self. quadro = ttk. Frame(self)
        self.botao = ttk.Button(self.quadro, text="Adiciona novo contador", command=self.adiciona_contador)
        self.botao.pack()
        self.quadro.pack(expand=True)

    def adiciona_contador (self): 
        novo_contador = Contador (len(self.contadores) + 1, master=self. quadro)
        self.contadores.append (novo_contador)

raiz = Aplicação () 
raiz.mainloop()
