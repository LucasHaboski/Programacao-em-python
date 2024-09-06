#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
#vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

nome = str(input('Digite o seu nome: '))

# Cabeçalho Banco
print('\n\n\n\n')
print('='*35)
print('BEM VINDO(A) {}{}{} AO SEU {}BANCO DIGITAL{} !'.format('\033[35m', nome[:nome.find(' ')], '\033[m','\033[32m', '\033[m')) # Roxo e LimpaCor, Verde e LimpaCor
print('='*35)

print('\nPercebemos que deseja fazer um empréstimo para comprar uma casa :D, vamos verificar se podemos aprovar..')

#Entrada dos dados
casa = float(input('\nDigite o valor da casa desejada: '))
sal = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos vai pagar a casa: '))

#Calculo prestação mensal
casa_mes = casa / (anos*12)

print('\n\nPara pagar uma casa de {}R${:.2f}{} em {}{}{} anos:'.format('\033[32m', casa,'\033[m', '\033[36m', anos, '\033[m'))
print('A prestação será de: {}R${:.2f}{}'.format('\033[33m', casa_mes,'\033[m'))

#Condicionas 
if (sal*0.3) >= casa_mes:
    print('\n\nParabens {}{}{}, o seu empréstimo foi {}APROVADO{} !!! :D'.format('\033[35m', nome, '\033[m', '\033[32m', '\033[m'))
else:
    print('\n\nInfelizmente {}{}{}, o seu empréstimo foi {}NEGADO{} ;-;'.format('\033[35m', nome, '\033[m', '\033[31m', '\033[m'))