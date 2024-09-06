#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario
#tentar descobrir qual foi o numero escolhido pelo computador. 
#O programa deverá escrever na tela se o usuario ganhouou perdeu

from random import randint

print('='*40)
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
print('='*40)

print('\nEscreva um palpite entre 0 e 5 e descubra se acertou..')
print('Gerando numero...')
num = randint(0,5)
print('\nNumero gerado!\n')

resp = int(input('Digite o seu palpite: '))

if resp == num:
    print('Voce acertou!!! o numero era: {}!'.format(num))
else:
    print('Infelizmente você errou ;-;\nO numero era {}!'.format(num))