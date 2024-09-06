i = 1

while i < 10:
    print(i)
    i += 1
print('Fim!')

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par,impar))    
print('Fim!')

r = 'S'
while r == 'S':
    r = str(input('Deseja continuar? [S/N]')).upper()
print('Fim do programa!')
