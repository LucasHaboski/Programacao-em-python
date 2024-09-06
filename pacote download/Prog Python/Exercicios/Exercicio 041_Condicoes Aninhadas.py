# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SêNIOR
# - Acima: MASTER

print('='*48)
print('{}VEJA QUAL CATEGORIA VOCÊ PERTENCE POR IDADE{}'.format('\033[36m','\033[m'))
print('='*48)

idade = int(input('Digite a sua idade: '))

if  idade > 0 and idade <= 9:
    print('Sua categoria é: {}MIRIM{}'.format('\033[32m','\033[m'))    # Cor: Verde
elif idade > 9 and idade <= 14:
    print('Sua categoria é: {}INFANTIL{}'.format('\033[34m','\033[m')) # Cor: Azul Escuro 
elif idade > 14 and idade <= 19:
    print('Sua categoria é: {}JUNIOR{}'.format('\033[33m','\033[m'))   # Cor: Amarelo
elif idade > 19 and idade <= 20:
    print('Sua categoria é: {}SÊNIOR{}'.format('\033[35m','\033[m'))   # Cor: Roxo
elif idade > 20:
    print('Sua categoria é: {}MASTER{}'.format('\033[36m','\033[m'))   # Cor: Azul Claro
else:
    print('\n{}VOCÊ DIGITOU UM VALOR INVALIDO, TENTE NOVAMENTE!{}'.format('\033[31m', '\033[m'))  # Cor: Vermelho