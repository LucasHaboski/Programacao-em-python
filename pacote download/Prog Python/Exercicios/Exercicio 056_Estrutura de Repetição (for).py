# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre: 
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

#importando bibliotecas
import os
from time import sleep

#Cabeçalho
os.system('cls')
print('='*33)
print('VERIFICADOR DE DADOS DE UM GRUPO')
print('='*33)

#Explicação exercicio
sleep(1)
print('\nO programa vai ler dados de 4 pessoas e mostrar informações sobre o grupo todo...')
sleep(2)
print('Vamos começar! ')
sleep(1)

m_idade = 0
hom_id = 0
mu_20 = 0

#Laço de repetição
for i in range (0,4):
    #Input dos dados
    nome = str(input('\n{} - Digite o seu {}nome{}: '.format(i+1,'\033[36m', '\033[m'))).strip()
    idade = int(input('{} - Digite a sua idade {}{}{}: '.format(i+1,'\033[36m', nome,'\033[m')))
    sexo = int(input('{} - Nos informe o seu sexo\n[1] - {}Masculino{}\n[2] - {}Feminino{}\nResposta: '.format(i,'\033[36m','\033[m','\033[33m','\033[m')))

    #Proteção apenas para o caso de digitar o sexo invalido
    if sexo < 1 and sexo > 2:
        print('{}Você digitou um valor Invalido, faça novamente.{}'.format('\033[31m','\033[m'))
        sexo = int(input('{} - Nos informe o seu sexo\n[1] - Masculino\n[2] - Feminino\nResposta: '.format(i+1,'\033[36m','\033[m','\033[33m','\033[m')))
        os.system('cls')
    else:
        #Testando que é o mais velho dentro dos homens
        if sexo == 1 and idade > hom_id:
            nome_v = nome
            hom_id = idade
        elif sexo == 1 and idade <= hom_id:
            nome_v = nome_v
            hom_id = hom_id
        
        #Fazendo um contador de quantas mulheres abaixo de 20 anos existe no grupo
        if sexo == 2 and idade < 20:
            mu_20 += 1

        #Contador para fazer a média de idades
        m_idade += idade

#Printando os resultados 
os.system('cls')
sleep(1)
print('{}RESULTADOS PRONTOS... {}'.format('\033[32m','\033[m'))
sleep(3)
print('\nA média de {}idade{} do grupo é: {}{}{}'.format('\033[35m','\033[m','\033[35m', m_idade/4, '\033[m'))
print('O {}homem{} mais velho do grupo é o: {}{} ({}anos){}'.format('\033[36m','\033[m','\033[36m', nome_v, hom_id,'\033[m'))
print('No grupo existe {}{} mulheres{} abaixo dos 20 anos!'.format('\033[33m', mu_20,'\033[m'))
