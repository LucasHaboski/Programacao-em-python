# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuario
# Quer ou não continuar, no final mostre:
#
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

#Importando Bibliotecas
import os
from time import sleep

#Cabeçalho
os.system('cls')
print('='*25)
print('{}CADASTRO DE FUNCIONARIOS{}'.format('\033[35m','\033[m'))
print('='*25)
sleep(1)

#Explicação do programa
print('\nO programa ira ler o {}nome{}, {}idade{} e {}sexo{} de diversas pessoas, '
      'ao final do programa irá mostrar estatisticas conforme as informações dadas'.format('\033[32m','\033[m','\033[36m','\033[m','\033[34m','\033[m'))

sleep(3)
print('\n{}VAMOS COMEÇAR..{}\n'.format('\033[32m','\033[m'))
sleep(2)

#Contadores (normal, maiores de idade, homens, mulheres abaixo de 20)
i = 0
i_mai = 0
i_man = 0
i_wom20 = 0

while True:

    #Definindo variavel de flag para TRUE 
    resp = 'A'
    idade = -1
    sexo = 'T'

    print('='*30)

    #Input do Nome
    nome = str(input('\nPessoa {} digite o seu {}nome{}: '.format(i+1, '\033[32m','\033[m')))

    #Protegendo a entrada de dados + Input idade
    while idade < 0:
        idade = int(input('{} qual a sua {}idade{}: '.format(nome, '\033[36m','\033[m')))
        if idade < 0:
            print('\n{}VOCÊ DIGITOU UMA IDADE INVALIDA, TENTE NOVAMENTE!\n{}'.format('\033[31m','\033[m'))

    #Protegendo a entrada de dados + Input sexo
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('{}, agora nos informe o seu {}sexo{} [M/F]: '.format(nome, '\033[34m','\033[m'))).upper()
        if sexo != 'M' and sexo != 'F':
            print('\n{}VOCÊ DIGITOU UMA ENTRADA INVALIDA, TENTE NOVAMENTE!\n{}'.format('\033[31m','\033[m'))

    if idade > 18:
        i_mai += 1

    if idade < 20 and sexo == 'F':
        i_wom20 += 1
    
    if sexo == 'M':
        i_man += 1
    
    i += 1

    print('\n{}DADOS CADASTRADOS!{}'.format('\033[32m','\033[m'))

    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja continuar [{}S{}/{}N{}]'.format('\033[32m','\033[m','\033[31m','\033[m'))).upper()
        if resp != 'S' and resp != 'N':
            print('\n{}VOCE DIGITOU UM VALOR INVALIDO, TENTE NOVAMENTE!{}'.format('\033[31m','\033[m'))

    if resp == 'N':
        break

#Visual printando resultado
print('\n\n{}GERANDO RESULTADOS. . .{}'.format('\033[35m','\033[m'))
sleep(2)
print('='*30)

#Printando resultado
print('\nPessoas cadastradas com {}mais de 18 anos{}: {}'.format('\033[36m', '\033[m',i_mai))
print('{}Homens cadastrados{}: {}'.format('\033[34m', '\033[m', i_man))
print('Mulheres com {}menos de 20 anos{}: {}'.format('\033[35m', '\033[m', i_wom20,))
sleep(5)

#Saindo do programa
print('\n\n{}==SAINDO DO PROGRAMA=={}'.format('\033[31m','\033[m'))
sleep(2)
