#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import floor

n = float(input('Digite um numero: '))

print('O numero {} tem a parte inteira {}'.format(n, floor(n)))