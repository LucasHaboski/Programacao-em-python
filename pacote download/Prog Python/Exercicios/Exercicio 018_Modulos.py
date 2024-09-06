#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import cos, tan, sin, radians

n = int(input('Digite um angulo e descubra o seno, cosseno e tangente: '))

s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(s, c, t))