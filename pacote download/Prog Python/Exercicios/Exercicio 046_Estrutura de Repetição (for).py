# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('='*30)
print('CONTAGEM REGRESSIVA ANO NOVO!!')
print('='*30)

for i in range(10, -1, -1):
    print('{}{}!{}'.format('\033[35m', i, '\033[m'))
    sleep(1)
print('\n\n{}F E L I Z   A N O   N O V O !!!!!!{}'.format('\033[33m', '\033[m'))
