#Crie um programa que leia dois numeros e mostre a soma entre eles

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

s = n1 + n2

print('A soma entre {} e {} é = {}!'.format(n1, n2, s)) #Essa é uma forma, criando uma variavel para soma

print('\n\nA soma entre {} e {} é = {}!'.format(n1, n2, n1+n2)) #Essa é outra forma somando as variaveis no print