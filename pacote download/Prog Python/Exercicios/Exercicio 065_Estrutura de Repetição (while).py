# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
 
#Importando Biblioteca
import os
from time import sleep

# Cabeçalho
os.system('cls')
print('='*34)
print('PROGRAMA DE {}MAIOR{} / {}MENOR{} E {}MEDIA{} '.format('\033[34m','\033[m','\033[36m','\033[m','\033[35m','\033[m'))
print('='*34)
sleep(2)

#Esplicando o Porgrama
print('\n\nO programa vai ler diversos numeros até o usuario {}não desejar continuar{}.'.format('\033[31m','\033[m'))
sleep(2)
print('\nAssim que o usuario parar de digitar o programa mostrara '
      'na tela o {}maior{}, o {}menor{} e a {}media{} dos valores lidos'.format('\033[34m','\033[m','\033[36m','\033[m','\033[35m','\033[m'))

#Fake start + wait
sleep(4)
print('\n{}Vamos começar...{}\n'.format('\033[32m','\033[m'))
sleep(1)

#Iniciando as variaveis necessarias
resp = 'S'
media = maior = 0
menor = 9999
i= 0 

#Enquanto o usuario desejar continuar digitando numeros o loop vai funcionar
while resp == 'S':

    sleep(1)
    os.system('cls')

    #Input do dado
    num = int(input('Digite o {}{}° numero{}: '.format('\033[32m', i+1,'\033[m')))

    #Protegendo o código para não digitar valores negativos
    if num > 0:

        if num > maior:
            maior = num

        elif num < menor:
            menor = num

        else:
            maior = maior
            menor = menor

        #Adicionando num na média + contador para calcular a média e printar no Input de dados
        media += num
        i += 1
    
    #Verificando se o usuario deseja continuar digitando valores
    resp = str(input('\nDeseja digitar mais numeros? [{}S{}/{}N{}]'.format('\033[32m','\033[m','\033[31m','\033[m'))).upper()

#Print do resultado + Fim do programa
if resp == 'N':
    os.system('cls')

    sleep(1)
    print('{}Maior{} numero: {}{}{} .'.format('\033[34m','\033[m','\033[34m', maior,'\033[m'))
    sleep(1)
    print('{}Menor{} numero: {}{}{} .'.format('\033[36m','\033[m','\033[36m', menor,'\033[m'))
    sleep(1)
    print('{}Media{} : {}{:.2f}{} .'.format('\033[35m','\033[m','\033[35m', media/i,'\033[m'))
    sleep(2)
    
    print('{}\n\n==SAINDO DO PROGRAMA==\n{}'.format('\033[31m','\033[m'))
    sleep(1)
    