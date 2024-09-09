# Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final mostre:
#
# A) Qual é o total gasto nas compras
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

import os
from time import sleep

# Cabeçalho
os.system('cls' if os.name == 'nt' else 'clear')  # 'nt' é para Windows, 'clear' é para Unix-based
print('='*20)
print('{}MERCADINHO MINIPRECO{}'.format('\033[36m','\033[m'))
print('='*20)
sleep(1)

# Explicação Programa
print('\nO usuario ira digitar o {}NOME{} e o {}PREÇO{} de diversos produtos.'
      '\nNo final, o programa ira mostrar informações sobre a sua compra'.format('\033[35m','\033[m', '\033[32m','\033[m'))

# Wait
sleep(3)
print('\n{}VAMOS COMEÇAR. . .{}\n'.format('\033[34m','\033[m'))
sleep(2)

tot_compra = 0
compra_1k = 0
maior_preco = 0
prod_caro = ''  # Definindo uma string vazia para o produto mais caro

while True:
    nome = input('\nDigite o {}NOME{} do produto: '.format('\033[35m','\033[m'))
    preco = float(input('Agora digite o {}PRECO{}: R$'.format('\033[32m','\033[m')))

    tot_compra += preco

    if preco > 1000:
        compra_1k += 1

    if preco > maior_preco:
        prod_caro = nome
        maior_preco = preco

    print('='*30)
      
    resp = input('\nQuer continuar as compras? [{}S{}/{}N{}]: '.format('\033[32m','\033[m','\033[31m','\033[m')).lower()

    print('='*30)

    if resp == 'n':
        break

print('='*30)
print('\nTotal gastos nas compras: {}{:.2f}{}'.format('\033[32m', tot_compra, '\033[m'))
print('Total de produtos que custam mais que R$1000,00: {}{}{}'.format('\033[35m', compra_1k, '\033[m'))
print('Produto mais caro: {}{}{}: R$ {:.2f}'.format('\033[34m', prod_caro, '\033[m', maior_preco))
