#Escreva um programa que leia um valor em metros e o exiba covertido em centimetros e milimetros

n = float(input('Digite um valor em metros: '))

print('\nValor em centimetros: {:.0f}cm\nValor em milimetros: {:.0f}mm'.format(n*100, n*1000))