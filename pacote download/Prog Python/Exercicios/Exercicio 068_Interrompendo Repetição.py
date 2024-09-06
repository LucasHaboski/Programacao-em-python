# Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

#Importando Bibliotecas
import os
from time import sleep
from random import randint

# Cabeçalho
os.system('cls')
print('='*20)
print('{}JOGO DE PAR OU IMPAR{}'.format('\033[35m', '\033[m'))
print('='*20)
sleep(2)

#Explicação do jogo
print('\nJogo de Par ou Impar, o usuario vai escolher uma opção e jogar contra o {}computador{}'
      '\nO jogo acabará quando o {}computador{} gannhar do usuario.\n'.format('\033[36m','\033[m', '\033[36m','\033[m'))

sleep(3)
print('{}Vamo começar{}\n'.format('\033[32m', '\033[m'))
sleep(3)

#COntador de vitoria
cont_w = 0

while True:
      #LimpaTela
      os.system('cls')
      sleep(1)

      #Input de dados + escolha do computador se sera par ou impar
      resp = int(input('Digite a sua jogada!\n[1] {}impar{}\n[2] {}par{}\nResposta: '.format('\033[34m', '\033[m','\033[35m', '\033[m')))  
      resp_c = randint(1,2)

      #Visual para a jogada
      sleep(2)
      print('\n{}Tudo pronto!{}\n\n'.format('\033[32m', '\033[m'))
      sleep(3)
      os.system('cls')
      print('{}PAAAR...{}'.format('\033[35m', '\033[m'))
      sleep(1)
      print('{}OOOU...{}'.format('\033[33m', '\033[m'))
      sleep(1)
      print('{}IIIMPAR!{}'.format('\033[34m', '\033[m'))
      sleep(1)

      #If o jogador acertar a escolha gerada pelo computador
      if resp == resp_c:
            print('\nVoce ganhou!!!\n{}Mais um ponto para voce!{}'.format('\033[32m', '\033[m'))
            sleep(2)
            cont_w += 1
      else:
            print('\nVoce {}perdeu{}! Finalizando o seu streak ;-;'.format('\033[31m', '\033[m'))
            break

#Print do Resultado
sleep(2)
print('='*25)
print('Sua sequencia de vitórias foi: {}{}{}'.format('\033[35m', cont_w,'\033[m'))
print('Continue jogando para aumentar o seu Streak :D')
print('='*25)

#Saindo do programa
print('\n\n{}==Saindo do programa=={}'.format('\033[31m', '\033[m'))
sleep(1)
