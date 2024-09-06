# Melhore o jogo do Exercicio 028_Condicional onde o computador vai "pensar" em um numero entre 0 e 10
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.

#Importando Bibliotecas
from random import randint
from time import sleep
import os

#LimpaTela
os.system('cls')

#Cabeçalho
print('='*22)
print('{}JOGO DE ADIVINHAÇÃO!!{}'.format('\033[32m', '\033[m'))
print('='*22)

sleep(2)

#Explicação do jogo
print('\nO computador vai sortear um numero de {}0 a 10{} e você deverá adivinhar, vamos começar!\n'.format('\033[31m', '\033[m'))

sleep(4)
os.system('cls')

#Visual de computador sorteando
for i in range(0, 2):
    print('{}Sorteando . {}'.format('\033[34m', '\033[m'))
    sleep(1)
    os.system('cls')
    print('{}Sorteando . .{}'.format('\033[34m', '\033[m'))
    sleep(1)
    os.system('cls')
    print('{}Sorteando . . .{}'.format('\033[34m', '\033[m'))
    sleep(1)
    os.system('cls')

#Sorteando o numero
num = randint(0,10) # sorteando de 0 a 10
print('='*16)
print('{}NUMERO SORTEADO!{}'.format('\033[32m', '\033[m'))
print('='*16)

sleep(3)

resp = 999 #Numero absurdo apenas para entrar no while
cont_t = 0 #Contador de quantos palpites 

#Loop até acertar o numero
while resp != num:
    os.system('cls')

    resp = int(input('\nDigite o Seu {}Palpite{}: '.format('\033[35m', '\033[m')))
    cont_t += 1

    if resp == num:
        print('Você {}ACERTOU{}!!\nTentativas: {}{}{}\nResposta: {}{}{}'.format('\033[32m', '\033[m', '\033[33m', cont_t,'\033[m', '\033[35m', num,'\033[m'))
    else:
        print('Você {}ERROU{}!'.format('\033[31m', '\033[m'))

        if resp < num:
            print('Dica: a resposta é um numero {}MAIOR{}, Tente novamente!'.format('\033[33m', '\033[m'))
        elif resp > num:
            print('Dica: a resposta é um numero {}MENOR{}, Tente novamente!'.format('\033[36m', '\033[m'))

    sleep(3)


print('\nFim do jogo, Parabens! :D')