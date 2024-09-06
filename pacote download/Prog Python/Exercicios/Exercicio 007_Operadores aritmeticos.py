#Faça um programa que leia duas notas de um aluno calcule e mostre a sua media

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
 
m = (n1 + n2) / 2.0
 
print('\nA media do aluno foi: {:.2f}'.format(m))