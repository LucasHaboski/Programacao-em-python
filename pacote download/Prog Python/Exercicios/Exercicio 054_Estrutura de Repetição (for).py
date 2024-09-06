# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores.

#biblioteca de LimpaTela
import os

#Cabeçalho
print('='*27)
print('VERIFICADOR DE MAIORIDADE!')
print('='*27)

#Inputs visuais apenas
print('\nVamos verificar a idade de 7 pessoas, e veremos quantos ja atingiram a maioridade')
pais = str(input('\nDigite o {}país{} em que voce reside: '.format('\033[35m', '\033[m')))
maior = int(input('Digite com quantos anos se atinge a maoiridade em {}{}{}: '.format('\033[35m', pais,'\033[m')))

#contador de pessoas
cont_m = 0

#repetição
for i in range(0,7):

    #input de dados
    nome = str(input('{}- Digite o seu {}nome{}: '.format(i+1, '\033[34m', '\033[m'))).strip()
    idade = int(input('{}- Digite a sua idade {}{}{}: '.format(i+1, '\033[34m', nome, '\033[m')))

    #Verificador de maioridade + contador para isso
    if idade > 0 and idade < 120:
        if idade >= maior:
            cont_m += 1
    else:
        print('{}Voce Digitou um valor invalido, Não será contado!{}'.format('\033[31m','\033[m'))
    print('\n')

#LimpaTela + print do resultado
os.system('cls')
print('No total das 7 pessoa do pais {}{}{} entrevistadas, {}{}{} são maiores de idade!'.format('\033[35m', pais,'\033[m','\033[32m', cont_m,'\033[m'))
