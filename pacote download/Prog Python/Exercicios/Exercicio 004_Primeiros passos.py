#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele.

n = input('Digite algo: ')

print("\n",type(n))

print('\nÉ pertencente ao alfabeto?', n.isalpha())
print('\nÉ pertencente ao numericos?', n.isnumeric())
print('\nÉ pertencente ao alfabeto ou numericos?', n.isalnum())
print('\nÉ escrito com a primeira letra maiuscula?', n.istitle())
print('\nÉ escrito só maiuscula?', n.isupper())
print('\nÉ escrito só mainuscula?', n.islower())
print('\nÉ escrito apenas com espaços?', n.isspace())