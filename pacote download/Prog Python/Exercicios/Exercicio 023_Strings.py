#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex Entrada: 1834
#Saida:
#unidade: 4
#dezena: 3 
#centena: 8
#milhar: 1

num = str(input('Digite um numero: '))

tamanho = len(num)

if tamanho == 4:

    print('\nMilhar: {}'.format(num[0]))
    print('Centena: {}'.format(num[1]))
    print('Dezena: {}'.format(num[2]))
    print('Unidade: {}'.format(num[3]))

elif tamanho == 3:
    
    print('\nCentena: {}'.format(num[0]))
    print('Dezena: {}'.format(num[1]))
    print('Unidade: {}'.format(num[2]))

elif tamanho == 2:

    print('\nDezena: {}'.format(num[0]))
    print('Unidade: {}'.format(num[1]))

else: 

    print('\nUnidade: {}'.format(num[0])) 

#outra possivel solução:

num_o = int(input('Digite um numero: '))

m = num_o // 1000 % 10
c = num_o // 100 % 10
d = num_o // 10 % 10
u = num_o // 1 % 10

print('\nMilhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))
