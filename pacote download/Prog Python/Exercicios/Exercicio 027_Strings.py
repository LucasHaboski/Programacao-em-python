#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeito e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro: Ana
#último: Souza

nome = str(input('Digite o seu nome completo: '))

print('Primeiro nome: {}'.format(nome[:nome.find(' ')]))
print('Último nome: {}'.format(nome[nome.rfind(' '):]))
