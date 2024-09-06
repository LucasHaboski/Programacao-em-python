#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario, com 15% de aumento

nome = str(input('Digite o nome do Funcionario: '))
sal = float(input('Digite o Salario do {}: R$'.format(nome)))

print("\n{} teve um aumento de 15%!!!\n\nAgora o salario do {} é: R${:.2f}".format(nome, nome, sal*1.15))