# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Importando biblioteca
import os

#Limpatela
os.system('cls')

#input de dados
nome = str(input('Digite o seu nome: '))

#Definindo variavel para loop
sex = 'A'

#Enquanto a resposta for diferente e M ou F, o loop continuara perguntando
while sex != 'M' and sex != 'F':
    sex = str(input('Nos informe o seu sexo [M/F]: ')).upper()

    if sex != 'M' and sex != 'F':
        print('{}Resposta Invalida, tente novamente!{}'.format('\033[31m', '\033[m'))

#Printando o resultado para cada caso
if sex == 'M':
    print('\nBem vindo {}{}{}!'.format('\033[34m', nome,'\033[m'))
else:
    print('\nBem vinda {}{}{}!'.format('\033[31m', nome,'\033[m'))
