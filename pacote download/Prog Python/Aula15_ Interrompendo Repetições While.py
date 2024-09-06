num = soma = 0

while True: #Infinito

    num = int(input('Digite um numero: '))
    
    if num == 999:
        break

    soma += num

print('A soma dos numeros digitados foram: {}'.format(soma))
print(f'A soma dos numero digitados foram: {soma}')  # f strings