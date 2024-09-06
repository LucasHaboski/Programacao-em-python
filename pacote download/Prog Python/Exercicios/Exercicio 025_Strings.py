#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

#primeira ideia
nome = str(input('Digite o seu nome: '))

nome_m = nome.upper()

tem = nome_m.find('SILVA')

if tem != -1:
    print('Tem Silva no nome!!!')
else:
    print('Não tem silva no nome')

#maneira mais coesa

nome2 = str(input('Qual o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('SILVA' in nome2.upper()))