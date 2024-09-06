# Refaça o Exercicio 009_Operadores Aritmeticos, mostrando a tabuada de um número que o usuário escolher, só que agora utilizado laço for.

n = int(input('Digite um numero: '))

print('='*15)
print('TABUADA DO {}{}{}!'.format('\033[36m', n,'\033[m'))
print('='*15)

for i in range(10):
    print('{} x {} = {}{}{}'.format(n, i+1, '\033[36m', n*(i+1),'\033[m'))