""" 
 * Nome: Exemplos de Funções
 * Descrição: Ao final da aula, os alunos serão capazes de criar 
 *            Funções.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-11-06
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""
#Exemplo 1
#Funcao sem passagem de parametros e sem retorno
def soma():
    n1 = int(input("Digite Valor : "))
    n2 = int(input("Digite Valor : "))
    print(n1+n2)
soma()

#Exemplo 2
#Funcao com passagem de parametros e sem retorno
def soma(a, b): 
    print(a+b)
soma(2,7)

#Exemplo 3
#Funcao sem passagem de parametros e com retorno
def soma(): 
    n1 = int(input("Digite Valor : "))
    n2 = int(input("Digite Valor : "))
    return n1+n2
print(soma())

#Exemplo 4
#Funcao com passagem de parametros e com retorno
def soma(a, b): 
    return a+b
print(soma(2,7))

#Exemplo 5
def máximo(a, b): 
    if a > b: 
        return a 
    else: 
        return b 
print(f"máximo(5,6) == 6 -> obtido: {máximo(5,6)}") 
