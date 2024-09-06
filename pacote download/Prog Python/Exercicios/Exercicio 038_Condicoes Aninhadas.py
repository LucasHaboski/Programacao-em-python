#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não Existe valor maior, os dois são iguais

#Entrada de dados
n1 = int(input('Digite o {}primeiro{} numero: '.format('\033[36m', '\033[m')))
n2 = int(input('Digite o {}segundo{} numero: '.format('\033[35m', '\033[m')))

print('\n') # Quebra de linha

#Possibilidades:
if n1 > n2:
    print('O {}PRIMEIRO{} valor é o maior!'.format('\033[36m', '\033[m'))
elif n1 < n2:
    print('O {}SEGUNDO{} valor é o maior!'.format('\033[35m', '\033[m'))
else:
    print('Os dois valores são {}IGUAIS{}!'.format('\033[32m', '\033[m'))