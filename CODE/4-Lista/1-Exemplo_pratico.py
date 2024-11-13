""" 
 * Nome: Exemplos de Lista
 * Descrição: Ao final da aula, os alunos serão capazes de criar 
 *            Listas.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-11-13
 * Versão: 2.0
 * 
 * Dependências:
 * - Python 3.12.6
"""

#Exemplo 001
#List (Similar a Vetor)
#Indexando / Atribuir valor a lista 
numbers = [10, 5, 7, 2, 1]
print("Os numeros  ", numbers)
print()
numbers[0] = 111
print("Os numeros ", numbers)
print()
print(numbers[3]) #imp 2
print()
numbers[1] = numbers[4]
print("Os numeros ", numbers)


#Exemplo 002
#Uma lista pode conter N tipos de dados 
my_list = [1, 3.20, True, "I am a string", 256, 0]
print(my_list)  # outputs: [1, 3.20, True, 'I am a string', 256, 0] 


#Exemplo 003
#Funcao len() Imprimindo o comprimento da lista
numbers = [10, 5, 7, 2, 1]
print("O numeros ", numbers)
print ("\n List length:", len (numbers))

#Exemplo 004
# Removendo o segundo elemento da lista.
numbers = [10, 5, 7, 2, 1]
print("O numeros ", numbers)
del numbers[1]
print("O numeros ", numbers)


#----------------------------------------------
#Funcoes X Metodos / com lista
#----------------------------------------------
#exemplo: funcao
#result  = function(arg)
#exemplo: metodo
#result = data.method(arg)

#Exemplo 005
#Novo elemento a lista 
numbers = [10, 5, 7, 2, 1]
print("Os numeros ", numbers)
print()
numbers.append (4) #novo elemento fim da lista
print("Os numeros ", numbers)
print()
numbers.insert (0, 222)#insert elemento
print("Os numeros ", numbers)
print()

#Exemplo 006 
l = [7,8,48,30]
print("Lista l")
print(l)
print("\n")
v = l
print("Lista l")
print(l)
print("Lista v")
print(v)
l[0]=77
print("Lista l")
print(l)
print("Lista l")
print(v)
print("\n")
#As duas lista apontam para o mesmo endereco de memoria 

#Exemplo 007
a = [7,8,48,30]
print("Lista a")
print(a)
print("\n")
b = a[:]  #copia dos elementos da lista 
print("Lista a")
print(a)
print("Lista b")
print(b)
b[0]=77  #altera elemento da lista b
print("Lista a")
print(a)
print("Lista b")
print(b)

#Exemplo 008
x = [7,8,48,30]
print("Lista x")
print(x)
x.append(99) 
print("Lista x com 99 no fim ")
print(x)
x = x+[999]
print("Lista x com 999 no fim ")
print(x)
x += [100]
print("Lista x com 100 no fim ")
print(x)
x = [55]+x
print("Lista x com 55 no inicio ")
print(x)


#Exemplo 009
#Criando uma lista vazia.
my_list = [] # Criando uma lista vazia.
for i in range(5):
   my_list.append (i + 1)
print (my_list)

#Exemplo 010
total = 0
my_list = [] # Criando uma lista vazia.
for i in range(5):
   my_list.append (i + 1)
print(my_list)
for i in range(len(my_list)):
    total += my_list[i]
print(total)


#Exemplo 011
list = [10,1,8,3,5]# tamanho 5
total = 0
for i in list:
    print(i)
    total += i
print(total)



total = 0
my_list = [] # Criando uma lista vazia.
for i in range(5):
   my_list.append (i + 1)
print(my_list)
for i in my_list: #i é o elemento da lista
    total += i
print(total) #soma dos elementos da lista

#Exemplo 012
#O Python oferece uma maneira mais conveniente de fazer a troca
#variable_1, variable_2 = variable_2, variable_1
#troca em Lista
my_list = [10, 1, 8, 3, 5]
print(my_list)
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1] 
print(my_list)


#Exemplo 013
notas = [6,7,5,8,9]
soma = 0
x = 0
while x < 5:
    soma += notas[x] 
    x += 1 
print(f"Media: {soma/x}")


#Exemplo 014
notas = [0,0,0,0,0]
soma = 0
x = 0
while x < 5:
    notas[x]=float(input(f"Nota {x}:"))
    soma += notas[x]
    x+=1
x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]}")
    x += 1
print(f"Media: {soma/x}")


#Exemplo 015
#Index negative
numbers = [111, 7, 2, 1]
print(numbers[-1]) #Ultimo da lista 1
print(numbers[-4]) #primeiro da lista 111


#Exemplo 016
list_1 = [5, 3, 1, 2, 4]
list_2 = list_1 #identificam o mesmo local na memória do computador.
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()
#Modificar um deles afeta o outro e vice-versa
list_1[2] = 99
print()
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()

#Exemplo 017
#Copia o conteúdo da lista, não o nome da lista..
#my_list[start:end] #lembrando end-1, [valor do indice:valor do indice-1]
list_1 = [5, 3, 99, 2, 4]
list_2 = list_1[:] # Copiar a lista inteira.
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()
list_2[3] = 95
print()
print("lista 1")
print(list_1)
print()
print("lista 2")
print(list_2)
print()

#Exemplo 018
my_list = [10, 8, 6, 4, 2]
print(my_list)
new_list = my_list[1:5]  # Copiando parte da lista.
print(new_list)
new_list = my_list[1:4] # Copiando parte da lista.
print(new_list)

#Exemplo 019
my_list = [10, 8, 6, 4, 2]
print(my_list)
new_list = my_list[1:-1]
print(new_list) #[8, 6, 4]

#Exemplo 020
#Se o start especificar um elemento além do descrito no end
#(do início da lista), a fatia estará vazia:

my_list = [10, 8, 6, 4, 2]#A fatia anda da direita para esquerda
new_list = my_list[-1:1] #[]
print(new_list) 
new_list = my_list[-1:-4] #[]
print(new_list) 


#Exemplo 021
my_list = [10, 8, 6, 4, 2]# A fatia anda da direita para esquerda
new_list = my_list[-4:-2]
print(new_list) #[8, 6]

#Exemplo 022
my_list = [1, 2, 3, 4]
print(my_list[-3:-2]) #[2]

#Exemplo 023
#excluir elementos da lista
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list) #[10, 4, 2]

#Exemplo 024
#lista vazia
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


#Exemplo 025
#The bubble sort
#Em python temos o metodo de ordenacao SORT
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)


#Exemplo 026
#Há também um método de lista chamado reverse(),
#que você pode usar para reverter a lista
lst = [5, 3, 1, 2, 4]
print(lst)
print()
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

#Exemplo 027
#par impar com lista
numbers = [12, 37, 5, 42,8,3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
