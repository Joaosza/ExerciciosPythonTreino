''' 1 '''

#Vt = Valor Temporario.
print("Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.\n")
f = input("Digite o valor de Farenheit : ")
f = float(f)
vt = f-32
c = 5 * vt / 9

print("Resultado", c)
print("\n")

''' 2 '''

print("Tendo como dados de entrada a altura e peso de uma pessoa, construa um algoritmo que calcule seu IMC, usando a seguinte fórmula: imc = peso ÷ altura²\n")

p = float(input("Informe o Seu Peso em Kg : "))
a = float (input("Informe a sua Altura em metros : "))

imc = p / a ** 2

print("O imc é ", imc)
print("\n")

''' 3 '''

print("Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.\n")
v = int(input("Informe um valor : "))

if v >= 0:
    print("Positivo")
else:
    print("Negativo")

print("\n")

''' 4 '''

print("Construa um programa que receba três valores, A, B e C. Em seguida, apresente na tela somente o maior deles.\n")

n1 = int(input("Informe o valor do Primeiro Numero : "))
n2 = int(input("Informe o valor do Primeiro Segundo : "))
n3 = int(input("Informe o valor do Primeiro Terceiro : "))

if n1 > n2 and n3:
    print (n1, 'é o maior numero')
elif n2 > n1 and n3:
    print (n2,'é o maior numero')
elif n3 > n2 and n1:
    print (n3,'é o maior numero')

print("\n")

''' 5 '''

print("Faça algoritmos em Python, utilizando o while, que")
print("A. Apresente na tela os números de 1 a 100.")
print("B. Faça a soma dos números de 1 a 100 e apresente somente o resultado.")
print("C. Apresente na tela somente os números pares entre 1 e 100.\n ")


x = 1
soma = 0

while x <= 100:
    x = x + 1
    print("Numero : ", x)
    print("\n")
    soma = soma + x
    print("A soma dos numeros é :", soma)
    if x % 2 != 0:
        print ("Par")

print("\n")

'''
6
'''

print("\t ====== Menu Principal ======")
print("\t 1. Número par ou ímpar?")
print("\t 2. Potência X")
print("\t 3. Raiz quadrada de X")
print("\t 4. Sair\n")
m = int(input("Escolha uma das opções do menu : \n"))

if m == "1":
    pi = int(input("Informe o numer para saber se é Par ou Ímpar : "))
    if int(pi) % 2 == 0:
        print("O numero ",pi ,"é Par")
    else:
        print("O numero",pi ,"é Impar")

elif m == "2":
    p = int(input("Informe o numero para Potencia : "))
    p = 2 ** p
    print("Resultado = ", p)

elif m == "3":
    r = int(input("Informe a Raiz de x : "))
    r ** (1/2)
    print("resultado da Raiz", r)

elif m == "4":
    print("Sair.")

else:
    print("Opção errada.")
