#Faça um programa que leia um numero inteiro e mostre seu dobro seu triplo e sua raiz quadrada

n = int(input('Digite um numero: '))

print("Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}".format(n*2, n*3, n**(1/2)))