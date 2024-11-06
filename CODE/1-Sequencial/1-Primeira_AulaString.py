""" 
 * Nome: Exemplos de String
 * Descrição: Ao final da aula, os alunos serão capazes de usar String.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-10-06
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""
#Exemplo 1 
print(len("A"))
print(len("Douglas"))
print(len("Aula de Lógica"))
print(len(""))

#Exemplo 2
cidade = "São Paulo"
print(cidade)
print(cidade[0])
print(cidade[4])

#Exemplo 3
#Concatenação
fname = 'Douglas'
fullname = fname + 'Godoy'
print("\n Seu nome ",fullname)

#Exemplo 4
#Composição %d, %f e %s
idade = 13
print("[%d]"%idade)
print("[%03d]"%idade)#três posições/completando com zeros à esquerda
print("[%3d]"%idade)#três posições/sem zeros à esquerda
print("[%-3d]"%idade)#Espacos em branco serão alinhados à direita

#Exemplo 5
nota = 7
#nota = 1_000 #Mil
#nota = 1_000_000 #Um Milhão 
print("[%5f]"%nota)
print("[%5.2f]"%nota)#5 representa cinco posições, sendo que duas são para parte decimal 
print("[%10.5f]"%nota)

print("%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34))

nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso."% (nome, idade, grana))

print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))

print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))

print( "%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))


#Exemplo 6
#Método format
nome = "Marcos"
idade = 28
grana = 81.34
print("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))

print("{:12} tem {:3} anos e R${:5.2f} no bolso.".format (nome, idade, grana))

print("{:12} tem {:03} anos e R${:5.2f} no bolso.".format(nome, idade, grana))

print("{:<125} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))

#Exemplo 7
print("{1} {0} {2}".format("a","b","c"))

print("{2} {2} {0} {1}".format("a","b","c"))

#f-string
nome = "Douglas"
idade = 35
grana = 101.00
print(f"{nome} tem {idade} anos e R${grana} no bolso.")

print(f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso.")

print(f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso.")

print(f"{nome:<125} tem {idade:<3} anos e R${grana:5.2f} no bolso.")

#Exemplo 8
#Fatiamento
s = "Introdução à Programação com Python"
#    0123456789
print(s)
print(len(s))
print(s[0:9])
print(s[0:11])
print(s[13:24])
print(s[29:35])

#Omitir o numero da esquerda ou direta
s = "Introdução à Programação com Python"
#    0123456789
print(s)
print(len(s))
print(s[:2])
print(s[1:])
print(s[:])

#Exemplo 9
s = "Introdução à Programação com Python"
#    0123456789
print(s)
print(len(s))
print(s[0:-2])
print(s[-1:])
print(s[-5:7])
print(s[-2:-1])

