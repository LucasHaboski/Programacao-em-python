# Crie um programa que leia vários numeros inteiros pelo teclado. O programasó vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

#Importando bibliotecas 
import os
from time import sleep

# Cabeçalho
os.system('cls')
print('='*25)
print('{}PROGRAMA DE SOMA COM FLAG{}'.format('\033[34m','\033[m'))
print('='*25)
sleep(1)

#Instruções do programa + perguntando se o usuario que ou não executa-lo
print('\nInstruções: O programa vai iniciar e você vai digitando numeros que deseja somar, quando não quiser mais, basta digitar o numero {}999{}!'.format('\033[31m','\033[m'))
sleep(3)
resp = str(input('\nVamos começar? [{}S{}/{}N{}] : '.format('\033[32m','\033[m','\033[31m','\033[m'))).upper()

if resp == 'S':

    #Iniciando variaveis para o loop + variavel de soma
    num = 0
    i = 1
    soma = 0
    print('\n\n')

    #Loop enquanto o usuario não digitar o flag "999"
    while num != 999:

        num = int(input('Digite o {}{}° numero{}: '.format('\033[35m',i,'\033[m')))

        #Caso não digite o flag, vai somar e somar 1 ao contador
        if num != 999:
            soma += num  
            i += 1  
    
    #Print resultado
    print('\nA soma dos {}{} numeros{} digitados foi: {}{}{}'.format('\033[35m',i-1,'\033[m','\033[36m',soma,'\033[m'))

    #Trocando a resposta para 'N' para sair printar o fim do programa
    resp = 'N'


#Digitou valor errado, sai do programa
elif resp != 'S' and resp != 'N':
    print('{}\nVOCE DIGITOU UM VALOR INVALIDO!!!\n\n==SAINDO DO PROGRAMA=={}'.format('\033[31m', '\033[m'))

#Caso não queia utilizar o programa
if resp == 'N':

    sleep(3)
    print('\n\n{}==FINALIZANDO PROGRAMA=={}'.format('\033[31m', '\033[m'))
    sleep(1)