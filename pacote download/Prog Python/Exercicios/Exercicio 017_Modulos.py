#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, pow

print('='*37)
print('Programa para calcular a hipotenusa')
print('='*37)

co = int(input('Escreva o comprimento do cateto oposto: '))
ca = int(input('Escreva o comprimento do cateto adjacente: '))

hip = sqrt(pow(co, 2) + pow(ca, 2))

print('\nA hipotenusa se calcula fazendo a raiz quadrada da soma dos catetos ao quadrado, logo: \n\nO comprimento da hipotenusa é: {:.2f}'.format(hip))
