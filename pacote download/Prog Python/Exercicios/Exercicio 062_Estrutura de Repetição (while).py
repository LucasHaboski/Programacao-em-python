# Melhore o Desafio 061_Estrutura de Repetição (while), perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que que mostrar 0 termos.

#Importando Bibliotecas
import os
from time import sleep

# Cabeçalho
os.system('cls')
print('='*28)
print('{}CALCULO DE TERMOS DE UMA PA{}'.format('\033[36m','\033[m'))
print('='*28)

sleep(1)

#Defiindo resposta para iniciar o loop + +input de dados
n = int(input('\nDigite o primeiro termo da sua P.A: '))
n_pa = n
raz = int(input('Agora digite a rezão da P.A: '))
i = 0

#Começando o print da P.A
sleep(1)
os.system('cls')
print('Os primeiros {}10 termos{} da sua P.A são: \n\n'.format('\033[33m','\033[m'))

#Loop printando a P.A e fazendo o calculo
while i < 10:

    if i < 9:
        print('{}{}{} - '.format('\033[35m', n_pa, '\033[m'), end = '')
    else:
        print('{}{}{} '.format('\033[35m', n_pa, '\033[m'))
    n_pa += raz
    i += 1

sleep(2)

#Vendo se o usuario deseja fazer mais termos da P.A
resp_s = str(input('\nDeseja ver mais termos da sua P.A? [{}S{}/{}N{}]\nResposta: '.format('\033[32m','\033[m','\033[31m','\033[m'))).upper()

#iniciando a condição (se o usuario deseja continuar)
if resp_s == 'S':

    sleep(1)
    os.system('cls')

    term = 1

    #Laço de repetição
    while term != 0:
        
        term = int(input('\nDigite quantos termos da sua P.A deseja ver: '))
        
        #Testando se o programa vai rodar ou não (quando o usuario digita 0, não quer mais ver)
        if term != 0 and term > 0:
            #LimpaTela
            sleep(1)
            os.system('cls')

            print('Os primeiros {}{} termos{} da sua P.A são: \n\n'.format('\033[33m', term, '\033[m'))

            #Printando a P.A com mais ou menos termos
            for i in range(0,term):
                
                if i < (term-1):
                    print('{}{}{} - '.format('\033[35m', n, '\033[m'), end = '')
                else: 
                    print('{}{}{} '.format('\033[35m', n, '\033[m'),)

                n += raz

            sleep(2)

            #Resetando o numero primario para o original
            n = n - (raz * term)

        #Caso digite 0 o programa vai mudar a resposta da pergunta "Deseja continuar?" para "N"
        else:
             resp_s = 'N'
    
#Printando Final do programa
if resp_s == 'N':

    print('\n\n{}==SAINDO DO PROGRAMA=={}'.format('\033[31m','\033[m'))
    sleep(2)
   