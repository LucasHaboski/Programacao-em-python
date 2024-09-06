# Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999, que é a condição de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

#Importando biblioteca 
import os
from time import sleep

# Cabeçlho
os.system('cls')
print('='*27)
print('{}PROGRAMA DE SOMA COM FLAG!{}'.format('\033[35m','\033[m'))
print('='*27)
sleep(1)

#Explicação do programa + wait
print('\nO programa vai ler numeros e somar eles enquanto o usuario desejar, quando não quiser mais'
        'basta digita o numero: {}999{} que o programa irá parar!'.format('\033[31m','\033[m'))
sleep(3)
print('{}Vamos começar...{}\n'.format('\033[32m','\033[m'))
sleep(2)

#Iniciando variaveis de cont
i= 0
som = 0

#Inicialição do loop infinito
while True:
    #Input de dados
    num = int(input('\nDigite o {}{} numero{}: '.format('\033[34m', i+1, '\033[m')))
    #Caso digite o flag o programa vai parar
    if num == 999:
        break

    #Somando nas variaveis
    som += num
    i += 1
    sleep(1)

#print do resultado
sleep(1)
os.system('cls')
print('\nResultado: Com {}{} numeros digitados{}, a soma entre eles foi: {}{}!!{}'.format('\033[34m', i,'\033[m','\033[34m', som,'\033[m'))

#Fim do Programa
sleep(3)
print('\n\n{}===SAINDO DO PROGRAMA==={}'.format('\033[31m','\033[m'))
sleep(1)
