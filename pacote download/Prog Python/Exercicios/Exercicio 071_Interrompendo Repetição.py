# Crie um programa que simule o funcionamento de um caixa elettronico. No inicio, pregunte ao usuario qual sera o valor sacado(inteiro)
# E o programa vai informar quantas cedulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50 , R$20, R$10 e R$1

# Importando bibliotecas
import os
from time import sleep

# Cabeçalho
os.system('cls' if os.name == 'nt' else 'clear') 
print('='*24)
print('{}CAIXA ELETRONICO BRASIL{}'.format('\033[35m','\033[m'))
print('='*24)
sleep(1)

# Explicação do problema
print('\nO programa ira perguntar qual o {}VALOR DO SAQUE{} e informara quantas notas ira retornar.\n'.format('\033[32m','\033[m'))
sleep(2)

# Input do valor que deseja sacar
print('='*24)
valor = int(input('Digite o {}VALOR{} que deseja sacar: R$'.format('\033[32m','\033[m')))

# Definindo variaveis de contador de nota
cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1  = 0
valor_f = valor

while True:

    # Se tiver mais que 50 reais para sacar
    if valor_f >= 50:
        cont_50+= 1
        valor_f -= 50

    # Se tiver mais que 20 reais para sacar
    elif valor_f >= 20:
        cont_20+= 1
        valor_f -= 20

    # Se tiver mais que 10 reais para sacar
    elif valor_f >= 10:
        cont_10+= 1
        valor_f -= 10

    # Se tiver mais que 1 real para sacar
    elif valor_f >= 1:
        cont_1+= 1
        valor_f -= 1

    # Se tiver menos que 1 real ele sai do loop
    else:
        break

sleep(2)
print('\n')
print('='*24)
print('\n')

# Printando o resultado
print('Com o valor de {}R${}{} voce consiguirá: \n'.format('\033[32m',valor,'\033[m'))
sleep(1)
print('{}{} nota(s) de 50.{}'.format('\033[35m', cont_50, '\033[m'))
sleep(1)
print('{}{} nota(s) de 20.{}'.format('\033[34m', cont_20, '\033[m'))
sleep(1)
print('{}{} nota(s) de 10.{}'.format('\033[37m', cont_10, '\033[m'))
sleep(1)
print('{}{} moeda(s) de 1.{}'.format('\033[33m', cont_1, '\033[m'))

print('\n')
print('{}-=FINALIZANDO PROGRAMA=-{}'.format('\033[31m','\033[m'))
sleep(2)
