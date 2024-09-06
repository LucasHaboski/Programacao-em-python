#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

#solução meio na gambiarra
num = int(input('Digite um ano e descubra se ele é BISSEXTO: '))

aux = num // 100
bi = num - (aux * 100)

print(bi)

if bi % 4 == 0:
    print('O ano {} é BISSEXTO!!!'.format(num))
else: 
    print('O ano {} não é BISSEXTO!!!'.format(num))
