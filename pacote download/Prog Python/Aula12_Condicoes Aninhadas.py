nome = str(input('Digite o seu nome: '))

if nome == 'walle':
    print('Que nome diferente :D')
elif nome == 'E.V.A':
    print('Que nome bonito ! :D')
else:
    print('Seu nome é bem normal.-.')

print('Tenha um otimo dia {}{}{}!'.format('\033[35m', nome, '\033[m'))
