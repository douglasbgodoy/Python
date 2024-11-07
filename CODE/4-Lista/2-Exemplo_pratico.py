""" 
 * Nome: Exemplos de Dicionario
 * Descrição: Ao final da aula, os alunos serão capazes de usar as 
 *            estruturas de Dicionario.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-11-06
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""

tabela = {"alface":0.45,
          "Batata": 1.20}
print(tabela["alface"])
#print(tabela["manga"]) #Erro
print("manga" in tabela)
print("Batata" in tabela)

print(tabela.keys())
print(tabela.values())
