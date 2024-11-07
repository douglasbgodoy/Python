""" 
 * Nome: Exemplos de Arquivos
 * Descrição: Ao final da aula, os alunos serão capazes de criar 
 *            Arquivos.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-11-06
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""
#Exemplo 1
arquivo = open("numeros.txt","w")
for linha in range (1, 101):
    arquivo.write(f"{linha}\n")
arquivo.close()

#Exemplo 2 Abrir, ler e fechar
arquivo = open("numeros.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Exemplo 3 Uso With
with open("numeros.txt","r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
arquivo.close()
