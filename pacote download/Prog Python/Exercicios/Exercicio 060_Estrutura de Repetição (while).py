# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#Importando bibliotecas
from os import system
from math import factorial

system('cls')

#Cabeçalho
print('='*20)
print('{}CALCULO DE FATORIAL{}'.format('\033[35m','\033[m'))
print('='*20)

###Método 1 (mais facil)

#Input de dados + calculo fatorial pela biblioteca
num = int(input('\nDigite um numero: '))
fator = factorial(num)

#Printando o começo do fatoria end = '' para não quabrar a linha
print('\n{}{}! -> '.format('\033[36m',num), end = '')

#Loop printando os elementos do fator
while num != 0:

    if num > 1:
        print('{} x '.format(num), end = '')
    else: 
        print('{} '.format(num), end = '')

    num -= 1

#Printando o resultado da conta
print('= {}{}'.format(fator,'\033[m'))

##===============================================================================================##

###Método 2 (mais complicado)

num = int(input('\nDigite um numero: '))

#Variaveis de conta e um auxiliar para diferenciar o primeiro loop
fat = 0
aux = 0

#Printando o começo do fatoria end = '' para não quabrar a linha
print('\n{}{}! -> '.format('\033[36m',num), end = '')

#Loop printando os elementos do fator + fazendo a conta
while num != 0:

    if num > 1:
        print('{} x '.format(num), end = '')
    else: 
        print('{} '.format(num), end = '')

    #Diferenciando o primeiro loop
    if aux == 0:
        fat = num
        aux = 1
    else:
        fat = fat * num

    num -= 1

#Printando o resultado da conta
print('= {}{}'.format(fat,'\033[m'))