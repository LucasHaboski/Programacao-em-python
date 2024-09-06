#crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com toas as letra minusculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: '))

print('Nome em Maiusculas: {}'.format(nome.upper()))
print('Nome em Minusculas: {}'.format(nome.lower()))
print('Letras ao todo sem espaços: {}'.format(len(nome) - nome.count(' ')))
print('Letras no primeiro nome: {}'.format(len(nome[:nome.find(' ')]))) #nome.find(' ') funciona tambem