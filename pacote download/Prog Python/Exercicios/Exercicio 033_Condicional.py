#Faça um progra que leia três numeros e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

if n1 > n2 and n1 > n3:
    print('\nMaior: {}'.format(n1))
    if n2 > n3:
        print('Menor: {}'.format(n3))
    else:
        print('Menor: {}'.format(n2))

elif n2 > n1 and n2 > n3:
    print('\nMaior: {}'.format(n2))
    if n1 > n3:
        print('Menor: {}'.format(n3))
    else:
        print('Menor: {}'.format(n1))

elif n3 > n2 and n3 > n1:
    print('\nMaior: {}'.format(n3))
    if n2 > n1:
        print('Menor: {}'.format(n1))
    else:
        print('Menor: {}'.format(n2))

else:
    print('Algum dos numeros são iguais, tente novamente!')