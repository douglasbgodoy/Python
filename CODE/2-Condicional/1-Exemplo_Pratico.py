""" 
 * Nome: Exemplos de Estrutura condicional
 * Descrição: Ao final da aula, os alunos serão capazes de usar as 
 *            estruturas de Controle de Fluxo if, elif e else.
 * Autor: Douglas Baptista de Godoy
 * Data de Criação: 2024-09-14
 * Versão: 1.0
 * 
 * Dependências:
 * - Python 3.12.6
"""

#Exemplo 001 Operadores Relacionais
print(2==2)

#Exemplo 002
print(2!=2)

#Exemplo 003
n = int(input("Digite Numero: "))
print(n>100)

#Exemplo 004
n = int(input("Digite Numero: "))
print(n>=100)

#Exemplo 005
n = int(input("Digite Numero: "))
print(n<100)

#Exemplo 006
n = int(input("Digite Numero: "))
print(n<=100)


#Exemplo 007
x=10
if x>5:
    print("Maior que 5")
if x<10:
    print("Menor que 10")
if x==10:
    print("Igual 10")

#Exemplo 008
x=10
if x<10:
    print("less than - menor que ")
else:
    print("greater than or equal - maior ou igual")

#Exemplo 009
x=10
if x>5:
    print("x> 5")
if x>8:
    print("x>8")
if x>10:
    print("x> 10")
else:
    print("Else will be executed")

#Exemplo 010
#--elif
x=10
if x>5:
    if x==6:
        print(" x == 6")
    elif x ==10:
        print("x == 10")
    else:
        print("else elif")
else:
    print("else")

#Exemplo 011
a = 3
b = 2
if a%b == 0:
    print("par")
else:
    print("impar")

#Exemplo 012
x, y, z = 5, 10, 8
print("x, y, z")
print(x,y,z)
x, y, z = z, y, x
print(x,y,z)

#print("x>z",x>z)
#print((y - 5)==x)


#Exemplo 013
# Leia três números.
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
 
# Verifique qual dos números é o maior
# e passe-o para a variável de número_maior.
 
largest_number = max(number1, number2, number3)#max Maior min Menor
print(largest_number)
 
# Imprimir o resultado.
#print("O maior número é:", largest_number)

#Exemplo 014
income = float(input("Entre com os rendimentos anuais "))
if income < 85528:
 tax = income * 0.18 - 556.02
else:
    tax = (income  - 85528 )* 0.32 + 14839.02

if tax <= 0: 
    tax = 0.0
tax = round(tax, 0)
print("A taxa é:", tax, "thalers") 


#Exemplo 015
idade = int (input ("Digite a sua idade: "))
if idade>=18:
    print("A pessoa é maior de idade")
print("FIM DE PROGRAMA! ")


#Exemplo 016
idade = int(input ("Digite a sua idade:\n"))
if(idade>=18):
    print("A pessoa é maior de idade")
if(idade<18):
    print("A pessoa é menor de idade")
print("FIM DE PROGRAMA!")


#Exemplo 017
# Entrada de dados:
media = int(input("Digite a nota final do aluno: "))
# Processamento e saída de dados 
if(media>=50):
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado!")
print("FIM DE PROGRAMA")

#Exemplo 018
# Entrada de dados:
nota = float(input("Digite a nota do aluno\n"))
# Processamento dos dados:
if(nota>=9):
    print("conceito final: A")
elif(nota>=7):
    print("conceito final: B")
elif (nota>=6):
    print("conceito final: C")
elif(nota>=5):
    print("conceito final: D")
else:
    print("conceito final: F")


#Exemplo 019
# Vamos criar um programa que pergunta ao usuário um número inteiro qualquer e o 
#cprograma calcula automaticamente a tabuada de 1 até 10 desse número:
# Sem o uso do comando while:

# Recebendo o número do usuário:
numero = input ("digite um número para o cálculo de sua tabuada: \n")
# Convertendo o número para inteiro:
numero = int (numero)
# Exibindo a tabuada do número:
print(f" {numero} x 1 = {numero*1}")
print(f" {numero} x 2 = {numero*2}")
print(f" {numero} x 3 = {numero*3}")
print(f" {numero} x 4 = {numero*4}")
print(f" {numero} x 5 = {numero*5}")
print(f" {numero} x 6 = {numero*6}")
print(f" {numero} x 7 = {numero*7}")
print(f" {numero} x 8 = {numero*8}")
print(f" {numero} x 9 = {numero*9}")
print(f" {numero} x 10 = {numero*10}")

#Exemplo 020 operadores lógicos (and or not )

#Operador and
entrada_1 = True
entrada_2 = False
print(entrada_1 and entrada_2) 


entrada_1 = True
entrada_2 = True
print(f" {entrada_1} and {entrada_2} = {entrada_1 and entrada_2}")


print(((2*2+3) == 7) and ((2+2) != 3) and (5*2==10))
#         7                 4               10
#        True               True            True
#True



#Operador or
entrada_1 = False
entrada_2 = False
resultado = entrada_1 or entrada_2
print (resultado)


entrada_1 = True
entrada_2 = False
resultado = entrada_1 or entrada_2
print (resultado)



print(((2*2+3) == 6) or ((2+2)!=4) or ((1+9)!=10))
#         7               4             10
#        False            False        False
#False


entrada_1 = True
entrada_2 = False
entrada_3 = True
print((entrada_1 and entrada_2) or entrada_3)


#Operador not
entrada = True
resultado = not entrada
print(resultado)


entrada = False
resultado = not entrada
print (resultado)


entrada_1 = (2*5) > 3 # True
entrada_2 = 13 < 12 # False
entrada_3 = False
print(not ((entrada_1 and entrada_2) or (entrada_1 and entrada_3) ))
#                    False                         False
#                                   False
#True

#Exemplo 021
print("Para a pergunta a seguir responda apenas com sim ou não:")
resposta = input("Seu time de futebol venceu a última partida que ele disputou?\n")
if((resposta=="sim" )or(resposta=="Sim")):
    print("Que legal!")
    print("Você deve estar feliz.")
if ((resposta=="não") or(resposta=='Não')) :
    print("Que triste!")
    print("Você deve estar chateado.")
print("FIM DE PROGRAMA")

#Exemplo 022
# Cabeçalho
print('='*43)
print("Responda a pergunta a seguir com sim ou não")
print('='*43)
# Entrada de Dados:
resposta = input("Seu time venceu a última partida que ele disputou?\n")
# Processamento e saída de dados:
if((resposta=='Sim') or (resposta=='sim')): 
    print("Que legal, você deve estar feliz!") 
else:
    print("Que triste, você deve estar chateado")
print ("Fim de programa" )

#Exemplo 023 operadores relacionais
#Faca um programa que faca a seguinte sequencia de atividade
# Receba um valor do usuario e armazena na variavel num
# Receba outro valor do usuario e armazena na variavel comparacao
# Converte amabos valores recebido para inteiro
# Realiza a operacao resultado = 2 X num + 3
# Utilize os operadores logicos para comparar se o resultado é maior ou igual a comparacao 
#Entrada de Dados
num = int(input("Digite um numero qualquer: "))
comparacao = int(input("Digite um outro numero para realizar a comparacao: "))
#Processamento 
resultado = 2*num+3
print(f"O resultado da comparacao é: {resultado >= comparacao }")

#Exemplo 024 Cuidados ao comparar valores
print("1" == 1) #False 
print(1.0 == 1) #True
print("A" == "a") #False 
print(" A " == "A") #False
print(10/3 == 3.33) #False 
print(10/3 == 3.333333) #False
print(10/3) 
print(10/3 == 3.3333333333333335) #True
