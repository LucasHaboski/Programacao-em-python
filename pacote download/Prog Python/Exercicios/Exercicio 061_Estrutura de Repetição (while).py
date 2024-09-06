# Refaça o Exercicio 051_Estrutura de Repetição (for), lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da prograssão usando a estrutura while.

#Importando Bibliotecas
from time import sleep
import os


#Cabeçalho
os.system('cls')
print('='*15)
print('{}CALCULO DE P.A{}'.format('\033[34m','\033[m'))
print('='*15)

sleep(1)

#Input de Dados
n = int(input('\nDigite o primeiro termo que deseja começar sua PA: '))
raz = int(input('Agora digite a razão da sua PA: '))
i = 0

#Visual Dados Coletados + LimpaTela
sleep(1)
print('\n{}DADOS COLETADOS...{}'.format('\033[32m','\033[m'))
sleep(2)
os.system('cls')

print('Veja como ficou a Sua {}Progressão Aritimética{}: \n'.format('\033[34m', '\033[m'))

#Printando e calculando a PA
while i < 10:

    if i < 9:
        print('{}{}{} - '.format('\033[35m', n, '\033[m'), end = '')
    else:
        print('{}{}{} '.format('\033[35m', n, '\033[m'))
    n += raz
    i += 1

#Print dim do programa
sleep(4)
print('\n{}Saindo do Programa!{}'.format('\033[31m','\033[m'))
sleep(1)