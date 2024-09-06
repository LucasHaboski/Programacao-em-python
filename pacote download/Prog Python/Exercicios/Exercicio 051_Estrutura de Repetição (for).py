# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A . No final, mostre os 10 primeiros termos dessa progressão

import string

print('='*35)
print('PROGRAMA DE PROGRESSÃO ARITIMETICA')
print('='*35)

ini = int(input('\nDigite qual numero deseja começar sua PA: '))
raz = int(input('Digite qual será a razão da sua PA: '))

print('\nOs 10 primeiros da sua PA são: ')
j = ini
for i in range (0, 10):
    print('{}{}{}'.format('\033[32m', j,'\033[m'), end=' -> ')
    j += raz
print('F I M !')
