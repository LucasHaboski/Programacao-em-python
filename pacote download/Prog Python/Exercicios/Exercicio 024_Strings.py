#Crie um programa que leia o nome de uma cidad e diga se ela começa ou não com o nome "Santo"

cidade = str(input('Digite o nome da cidade: ')).strip()

sant = cidade.count('Santo ',0,6)

#metodo 1 sem muita proteção
if sant == 1:
    print('A cidade começa com Santo!')
else:
    print('A cidade não começa com Santo ;-;')

#metodo 2
print(cidade[:5].upper() == 'SANTO')