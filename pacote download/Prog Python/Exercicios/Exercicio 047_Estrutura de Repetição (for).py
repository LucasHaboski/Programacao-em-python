# Crie um programa que mostre todos os números pares que estão no intervalo entre 1 e 50.

#Cabeçalho
print('='*30)
print('NUMEROS PARES ENTRE 1 E 50!')
print('='*30)

#Forma com salto, testando apenas os pares
for i in range (2, 51, 2):
    print('{}{}{}!'.format('\033[34m', i, '\033[m'))
print('F I M !')

print('\n\nForma 2:\n')

#Forma passando por todos os numeros entre 1 e 50
for j in range (1,51):
    if j % 2 == 0:
        print('{}{}{}!'.format('\033[32m', j, '\033[m'))
print('F I M !')