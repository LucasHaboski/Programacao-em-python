# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for impar, desconsidere-o.

so = 0

for i in range (0,6):
    if i == 0:
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            so += n
    else: 
        n = int(input('Digite o próximo numero: '))
        if n % 2 == 0:
            so += n
print('\nA soma dos numeros pares digitados foi: {}{}{}'.format('\033[35m', so, '\033[m'))
