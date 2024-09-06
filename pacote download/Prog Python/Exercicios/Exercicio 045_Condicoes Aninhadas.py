### Crie um programa que faça o computador jogar Jokenpô com você.

#Importando bibliotecas
from random import randint
from time import sleep
import os

#Cabeçalho
print('='*30)
print('{}J O G O   D E   J O K E N P Ô{}'.format('\033[31m','\033[m'))
print('='*30)
sleep(2)

#Regras do Jogo
print('\nAs regras são simples:\nVoce tem que escolher alguma dessa opções ->\n1- {}PEDRA{}\n2- {}PAPEL{}\n3- {}TESOURA{}'
                                                    .format('\033[32m','\033[m','\033[34m','\033[m','\033[35m','\033[m'))

sleep(2)
print('\nBasicamente, uma opção ganha de outra, ficando da seguinte forma:\n')
sleep(2)
print('- {}PEDRA{}   ganha de {}TESOURA{}'.format('\033[32m','\033[m','\033[35m','\033[m'))
sleep(2)
print('- {}TESOURA{} ganha de {}PAPEL{}'.format('\033[35m','\033[m','\033[34m','\033[m'))
sleep(2)
print('- {}PAPEL{}   ganha de {}PEDRA{}'.format('\033[34m','\033[m','\033[32m','\033[m'))
sleep(2)

#Verificando se o usuario que jogar ou não (futuramente vai virar um laço de repetição)
resp = int(input('\nAgora que sabe as regras, deseja Jogar? \n1 -> YES\n2 -> NO\nEscolha: '))

#Proteção do código caso digite algo sem ser sim ou não
if resp == 1:
    os.system('cls')
    #Input da escolha do usuario
    player = int(input('\n\nEscolha uma das opções a baixo:\n1- {}PEDRA{}\n2- {}PAPEL{}\n3- {}TESOURA{}\nEscolha: '
                                            .format('\033[32m','\033[m','\033[34m','\033[m','\033[35m','\033[m')))

    #Fazendo o computador escolher uma opçaõ de jogada
    comp = randint(1,3)

    #Proteção do código caso o usuario digite algo diferente das opções(mais tarde vai virar um laço de repetição)
    if player > 0 and player < 4:

        #Transformando a escolha do jogador novamente em uma string para melhor visual no final
        if player == 1:
            simbolo = '\033[32mPEDRA\033[m'
        elif player == 2:
            simbolo = '\033[34mPAPEL\033[m'
        elif player == 3:
            simbolo = '\033[35mTESOURA\033[m'

        #Transformando a escolha do computador novamente em uma string para melhor visual no final
        if comp == 1:
            simbolo2 = '\033[32mPEDRA\033[m'
        elif comp == 2:
            simbolo2 = '\033[34mPAPEL\033[m'
        elif comp == 3:
            simbolo2 = '\033[35mTESOURA\033[m'

        print('\n{}JO{}'.format('\033[36m','\033[m'))
        sleep(1)
        print('{}KEN{}'.format('\033[34m','\033[m'))
        sleep(1)
        print('{}PO!!{}\n'.format('\033[35m','\033[m'))

        print('='*55)

        #Testando quem ganho o jogo!
        if player == 1 and comp == 2:
            print('Voce {}PERDEU{}!\n\nSua escolha -> {} x {} <- escolha do Computador.'.format('\033[31m','\033[m', simbolo, simbolo2))
        elif player == 2 and comp == 3:
            print('Voce {}PERDEU{}!\nSua escolha -> {} x {} <- escolha do Computador.'.format('\033[31m','\033[m', simbolo, simbolo2))
        elif player == 3 and comp == 1:
            print('Voce {}PERDEU{}!\nSua escolha -> {} x {} <- escolha do Computador.'.format('\033[31m','\033[m', simbolo, simbolo2))
        elif player == comp:
            print('Aconteceu um {}EMPATE{}!\nSua escolha -> {} x {} <- escolha do Computador.'.format('\033[33m','\033[m', simbolo, simbolo2))
        else:
            print('PARABENS, voce {}GANHOU{}!\nSua escolha -> {} x {} <- escolha do Computador.'.format('\033[32m','\033[m', simbolo, simbolo2))
        
        print('='*55)

    else:
        print('\n{}VOCE DIGITOU UM VALOR INVALIDO, TENTE NOVAMENTE!{}'.format('\033[31m','\033[m'))

elif resp == 2:
    print('\n{}Que pena... Quando quiser jogar basta reiniciar o programa :D{}'.format('\033[34m','\033[m'))
else:
    print('\n{}VOCE DIGITOU UMA RESPOSTA INVALIDA, REINICIE O PROGRAMA!{}'.format('\033[31m','\033[m'))
