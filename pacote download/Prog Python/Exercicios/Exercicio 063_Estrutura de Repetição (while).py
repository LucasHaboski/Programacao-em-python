# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequencia Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

#Importando bibliotecas
import os
from time import sleep

# Cabeçalho
os.system('cls')
print('='*23)
print('{}PROGRAMA DE FIBONACCI.{}'.format('\033[35m','\033[m'))
print('='*23)
sleep(2)

n_ele = int(input('\nDigite quantos elementos de {}Fibonacci{} deseja ver: '.format('\033[35m','\033[m')))

#Defininfo variaveis para o Fibonacci + variavel de cont
n1 = 0
n2 = 1 
r = n1 + n2
i = 0

#Limpatela + Calculando
os.system('cls')
print('\nOs primeiros {}{} termos{} de {}Fibonacci{} são: \n\n'.format('\033[32m', n_ele,'\033[m','\033[35m','\033[m'))
sleep(2)

#Laço de repetição para print + calculo de Fibonacci
while i < n_ele:

    #Printando a sequencia Fibonacci
    if i < (n_ele-1):
        print('{}{}{} '.format('\033[34m', n1, '\033[m'),end = '-> ')
    else:
        print('{}{}{} '.format('\033[34m', n1, '\033[m'))  
     
    #Realizando o calculo para o Fibonacci, encontrei essa forma substituindo os valores e somando, acredito que existam outras! + Soma para o contador
    n1 = n2
    n2 = r
    r = n1+n2
    i += 1

#Fim do Programa
sleep(4)
print('\n\n\n{}===FINALIZANDO O PROGRAMA==={}'.format('\033[31m', '\033[m'))
sleep(1)
