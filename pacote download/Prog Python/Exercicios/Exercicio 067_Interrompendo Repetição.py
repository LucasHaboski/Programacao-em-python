# Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuario.
#  O programa será interrompido quando o numero solicitado for negativo

#Importando Bibliotecas
import os
from time import sleep

# Cabeçalho
os.system('cls')
print('='*20)
print('{}PROGRAMA DE TABUADA{}'.format('\033[34m','\033[m'))
print('='*20)
sleep(1)

#Explicando O programa
print('\nO programa vai solicitar que digite um numero, e o mesmo vai te mostrar a tabuada do numero digitado.'
       '\nO programa ira parar quando o usuario {}digitar um numero negativo.{}\n'.format('\033[31m','\033[m'))
sleep(3)

#Repetindo até o usuario digitar o flag
while True:

    # Cabeçalho para o input de dado
    print('\n')
    print('-'*20)
    num = int(input('Digite um numero: '))
    print('-'*20)
    print('\n')

    #Flag
    if num < 0:
        break

    #Printando a tabuada
    for i in range(0,10):
        print('{} X {} = {}{}{}'.format(num, i+1, '\033[35m', num*(i+1), '\033[m'))
        sleep(1)

    sleep(1)

#Saindo do programa
print('\n\n{}==SAINDO DO PROGRAMA=={}'.format('\033[31m','\033[m'))
sleep(2)
