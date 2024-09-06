#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salarios superiores a R$1.250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

nome = str(input('Digite o nome do funcionario: '))
print('Ola {} Bem vindo ao sistema! Vamos calcular seu novo salario :D'.format(nome))

sal = float(input('\nDigite o seu salario atual: R$'))

if sal > 1250:
    print('\nParabens {}, você recebeu um aumento de 10%!!!\nSeu novo salario é: {:.2f}'.format(nome, sal*1.1))
else:
    print('\nParabens {}, você recebeu um aumento de 15%!!!\nSeu novo salario é: {:.2f}'.format(nome, sal*1.15))