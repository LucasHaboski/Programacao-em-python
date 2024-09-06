# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# Se ele ainda vai se alistar ao serviço militar 
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

#Cabeçalho
print('='*55)
print('{}BEM VINDO AO SERVIÇO DE ALISTAMENTO MILITAR OBRIGATÓRIO!{}'.format('\033[32m','\033[m'))
print('='*55)

#Input de dados
ano = int(input('\nDigite o ano que você nasceu: '))
idade = 2024 - ano

#Condiçoes
if idade < 18: 
    print('\nVocê irá se alistar no serviço militar em {}{} anos!{}'.format('\033[34m', 18 - idade,'\033[m'))
elif idade == 18:
    print('\n{}É HORA DE SE ALISTAR, SE APRESENTE NO BATALHÃO MAIS PRÓXIMO{}!'.format('\033[32m', '\033[m'))
else:
    print('\nO seu ano de alistamento ja passou, esta atrasado em: {}{} anos!{}'.format('\033[31m', idade - 18, '\033[m'))
    print('Seu alistamento foi em {}{}{}!!!'.format('\033[31m', ano + 18, '\033[m'))
