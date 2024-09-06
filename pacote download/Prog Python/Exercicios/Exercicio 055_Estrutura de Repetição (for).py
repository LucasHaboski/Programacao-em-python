# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#bibliotecas para wait e clean screen
from time import sleep
import os

#Cabeçalho
print('='*35)
print('VERIFICADOR DE PESO: MAIOR E MENOR')
print('='*35)

#Explicação exercicio para o usuario
print('\nNesse programa vamos ler o peso de 5 pessoas e mostrar qual foi o menor e maior peso lidos, vamos começar...\n')
sleep(2)

for i in range (0, 5):
    #Input de dados
    nome = str(input('Individuo 0{} -> Digite o seu {}nome{}:'.format(i+1, '\033[35m', '\033[m'))).strip()
    peso = float(input('\nBem vindo {}{}{}!\nNos informe o seu Peso (Kg): '.format('\033[35m', nome,'\033[m')))

    print('\n')

    #protegendo o codigo, (preciso ver como faço para diminuir o contador caso o usuario tiver digitado errrado)
    if peso > 0.0:
        #Primeiro loop, as variaveis vao receber o primeiro valor (valor padrão)
        if i == 0:
            #Definindo variaveis de maior e menor (tanto peso quanto nome)
            me_peso = peso
            ma_peso = peso
            me_nome = nome
            ma_nome = nome
        else:
            #Caso o valor digitado seja maior que o maior peso anterior
            if peso > ma_peso:
                ma_peso = peso
                ma_nome = nome
            #Caso a condição de cima seja falsa, e o valor digitado seja menor que o menor peso anterior
            elif peso < me_peso:
                me_peso = peso
                me_nome = nome
            #Caso nenhuma condição seja verdadeira, mantem o que ja estava
            else:
                me_peso = me_peso
                ma_peso = ma_peso
                me_nome = me_nome
                ma_nome = ma_nome
    else:
        #mensagem caso tenha digitado um valor invalido :O
        print('{}VOCE DIGITOU UM VALOR INVALIDO, SUA RESPOSTA NÃO SERÁ COMPUTADA{}'.format('\033[31m', '\033[m'))

#Visual
for i in range (0,2):
    os.system('cls') 
    #Visual para "verificar" resultado
    print('{}VERIFICANDO .{}'.format('\033[34m', '\033[m'))  
    sleep(1)
    os.system('cls') 
    print('{}VERIFICANDO . .{}'.format('\033[34m', '\033[m'))  
    sleep(1)
    os.system('cls') 
    print('{}VERIFICANDO . . .{}'.format('\033[34m', '\033[m'))  
    sleep(1)
   

#Printando os resultados
os.system('cls')
print('-'*20)
print('{}RESULTADO PRONTO :D{}'.format('\033[32m','\033[m'))
print('-'*20)

sleep(2)

print('\n\nA pessoa com {}maior peso{} registrado foi: '.format('\033[35m', '\033[m'))
sleep(2)
print('Nome: {}{}{}\nPeso: {}{}Kg{}'.format('\033[35m', ma_nome,'\033[m','\033[35m', ma_peso,'\033[m'))

sleep(3)

print('\nA pessoa com {}menor peso{} registrado foi: '.format('\033[34m', '\033[m'))
sleep(2)
print('Nome: {}{}{}\nPeso: {}{}Kg{}'.format('\033[34m', me_nome,'\033[m','\033[34m', me_peso,'\033[m'))
