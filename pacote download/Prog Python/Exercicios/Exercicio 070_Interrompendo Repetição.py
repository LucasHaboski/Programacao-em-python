# Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final mostre:
#
# A) Qual é o total gasto nas compras
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

#Importando bibliotecas
import os
from time import sleep

#Cabeçalho
os.system('cls')
print('='*20)
print('{}MERCADINHO MINIPRECO{}'.format('\033[36m','\033[m'))
print('='*20)
sleep(1)

#Explicação Programa
print('\nO usuario ira digitar o {}NOME{} e o {}PREÇO{} de diversos produtos.'
      '\nNo final, o programa ira mostrar informações sobre a sua compra'.format('\033[35m','\033[m', '\033[32m','\033[m'))

sleep(3)
print('\n{}VAMOS COMEÇAR. . .{}\n'.format('\033[34m','\033[m'))
sleep(2)