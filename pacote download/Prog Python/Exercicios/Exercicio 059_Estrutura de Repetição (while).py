# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Numeros
# [5] Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada Caso

#Importando bibliotecas
import os
from time import sleep

os.system('cls')

#Cabeçalho
print('='*40)
print('{}ESCOLHA 2 NUMEROS E O QUE DESEJA FAZER!{}'.format('\033[35m', '\033[m'))
print('='*40)

#Definindo variavel para começar perguntando os numeros
resp = 4

#Loop enquanto o usuario não escolher sair
while resp != 5:

    if resp == 4:
        n1 = int(input('\nDigite um numero: '))
        n2 = int(input('Digite o um outro numero: '))

    sleep(1)
    os.system('cls')

    print('O que deseja fazer com os numeros {}{}{} e {}{}{}?\n'.format('\033[34m', n1, '\033[m', '\033[36m', n2, '\033[m'))
    #Escolhas
    print('[1] {}Somar{}'.format('\033[32m', '\033[m'))
    print('[2] {}Multiplicar{}'.format('\033[33m', '\033[m'))
    print('[3] {}Maior{}'.format('\033[35m', '\033[m'))
    print('[4] {}Novos Numeros{}'.format('\033[36m', '\033[m'))
    print('[5] {}Sair do Programa{}'.format('\033[31m', '\033[m'))
    #Input escolha
    resp = int(input('Sua escolha: '))
    sleep(1)
    os.system('cls')

    if resp == 1:
        print('A soma de {}{}{} e {}{}{} é: {}{}{}'.format('\033[34m', n1, '\033[m', '\033[36m', n2, '\033[m', '\033[32m', n1+n2, '\033[m'))
        sleep(2)
    elif resp == 2:
        print('A multiplicação de {}{}{} e {}{}{} é: {}{}{}'.format('\033[34m', n1, '\033[m', '\033[36m', n2, '\033[m', '\033[33m', n1*n2, '\033[m'))
        sleep(2)
    elif resp == 3:
        if n1 > n2:
            print('O maior numero entre {}{}{} e {}{}{} é: {}{}{}'.format('\033[34m', n1, '\033[m', '\033[36m', n2, '\033[m', '\033[35m', n1, '\033[m'))
            sleep(2)
        else:
            print('O maior numero entre {}{}{} e {}{}{} é: {}{}{}'.format('\033[34m', n1, '\033[m', '\033[36m', n2, '\033[m', '\033[35m', n2, '\033[m'))
            sleep(2)
    
    
print('{}SAINDO DO PROGRAMA..{}'.format('\033[31m', '\033[m'))
sleep(1)
