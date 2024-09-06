# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('='*30)
print('IDENTIFICADOR DE NUMERO PRIMO!')
print('='*30)

num = int(input('\nDigite um numero: '))

pri = 0

for i in range (1, num):
    if num % i == 0:
        pri+=1

if pri == 1:
    print('\nO numero {}{}{}: {} é primo!!{}'.format('\033[35m',num ,'\033[m','\033[32m','\033[m'))
else:
    print('\nO numero {}{}{}: {} NÃO é primo!!{}'.format('\033[35m',num,'\033[m','\033[31m', '\033[m'))
