# Crie um programa que leia uma frase qualquer e diga se ela é um Palíndromo (igual de tras para frente), desconsiderando os espaços.

#Importando biblioteca
from time import sleep
import os

#Cabeçalho
print('='*25)
print('VERIFICADOR DE PALINDROMO')
print('='*25)

#Lendo string e formatando ela para ficar minuscula e sem espaços
pala = str(input('\nDigite a sua frase\palavra: ')).strip().lower()#tira espaçoa da esquerda e direita | deixa tudo minusculo
sepa = pala.split() #Separa a frase em palavras separadas
junto = ''.join(sepa) #Junta as palavras sem espaço
tamanho = len(junto) #Tamanho da string

#Variaveis auxiliares
j  = tamanho -1
cont = 0

#Visual para "Comparar as duas strings"
os.system('cls')
print('Vamos verificar:\n')
sleep(1)
print('{}Normal{}:     {}Inverso{}:\n'.format('\033[32m','\033[m','\033[31m','\033[m'))
sleep(1)

#Verificando a igualdade das strings
for i in range(0, tamanho):
    print('   {}{}{}   ---   {}{}{}'.format('\033[32m', junto[i],'\033[m','\033[31m', junto[j],'\033[m'))
    sleep(1)

    #Contador para saber se a letra do indice i(0 -> tam) é igual a letra do indice j(tam -> 0)
    if junto[i] == junto[j]:
        cont += 1
    j -= 1

#Printando resultado
if cont == tamanho:
    print('\nResultado: A palavra {}{}{}...'.format('\033[34m', pala,'\033[m'))
    sleep(2)
    print('{}É palindromo!{}'.format('\033[32m', '\033[m'))
else: 
    print('\nResultado: A palavra {}{}{}...'.format('\033[34m', pala,'\033[m'))
    sleep(2)
    print('{}NÃO é palindromo!{}'.format('\033[31m', '\033[m'))
