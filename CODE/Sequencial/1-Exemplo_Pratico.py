#Exemplo 1
print("Ola mundo python")

#Exemplo 2
print('Ola mundo teste 2 em python')

#Exemplo 3
input()

#Exemplo 4
print("Digite o seu nome ")
input()

#Exemplo 5
input("Digite o seu nome: ")

#Exemplo 6
idade = 20 
print(type(idade))

#Exemplo 7
idade = "20" 
print(type(idade))

#Exemplo 8
altura = 1.87 
print(type(altura))

#Exemplo 9
altura = float("1.87") 
print(type(altura))

#Exemplo 10
idade = int(20.8)
print(type(idade))

#Exemplo 11
texto = str(20)
print(type(texto))

#Exemplo 12 
teste = True
print(type(teste))

#Exemplo 13
print(" Douglas \n Godoy")
print("Douglas", "Godoy")

#Exemplo 14
jonh=3
mary=5
adam=6
print(jonh, mary, adam, sep=',' )
total_apples = jonh + mary + adam
print(total_apples)

#Exemplo 15
print(0o123)
print(0x123)

print(11_111_11)

print(3E8)

#Exemplo 16
a = 2
b = 2
 
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#Exemplo 17
i=1
i = i + 1
print(i)
i += 1
print(i)


#Exemplo 18
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")


#Exemplo 19 
#Erro str and float
anything = input("Digite um numero ")
something = anything ** 2.0
print (anything, "elevado a 2 é",something)

# str and float
anything = float(input("Digite um numero "))
something = anything ** 2.0
print (anything, "elevado a 2 é",something)

#Exemplo 20 
fname = 'douglas'
lname = "godoy"
print("\n Seu nome "+fname+""+lname+".")

#Exemplo 21 
print("Logica"*3)

z = 2.5
print(type(z))

a = ((2**2)**3)#64
print(a)

b = 2**2**3 #leitura da direita 2^(2^3)= 256
print(b)


#Exemplo 22
x = 0
x = float(x)
y = (3*(x**3)) -(2 *(x**2)) +(3*x) -1
print("y =", y)


#Exemplo 23 
x = input("Digite um número: ") # O usuário digita 2
print(type(float(x)))

x = int(input())
y = int(input())
 
x = x // y
y = y // x

#Exemplo 24 IMC
#Entrada de Dados
altura = input("Digite a sua altura: ")
peso = input("Digite o seu peso: ")
idade = input("Digite a sua idade")
#Processamento 
altura = float(altura)
peso = float(peso)
idade = int(idade)
imc = peso /(altura*altura)
#Saida
print(imc)

#Exemplo 25 IMC
#Entrada de Dados
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
idade = int(input("Digite a sua idade"))
#Processamento 
imc = peso /(altura*altura)
#Saida
print(f"O seu IMC é igual à: {imc:.2f} e a sua idade é igual à: {idade}")
