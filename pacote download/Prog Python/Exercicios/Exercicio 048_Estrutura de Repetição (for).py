# Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 até 500

#Bibliotecas (wait and cls)
from time import sleep
import os

#Cabeçalho
print('='*66)
print('CALCULANDO TODOS OS NUMEROS IMPARES, MULTIPLOS DE 3 ENTRE 1 E 500')
print('='*66)

sleep(3)

#Print visual "Fazendo calculo"
for i in range(0,3):
    os.system('cls')
    print('Realizando calculo .')
    sleep(1)
    os.system('cls')
    print('Realizando calculo . .')
    sleep(1)
    os.system('cls')
    print('Realizando calculo . . .')
    sleep(1)
os.system('cls')
print('Calculo feito! \n\n')

#def da variavel
som = 0

#repetição para realizar a conta
for i in range(1,501, 2):
    if i % 3 == 0:
        som += i
print('A soma é: {}{}{}'.format('\033[32m', som, '\033[m'))
