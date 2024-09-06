# Refaça o Exercicio 035_Condicional dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('{}DIGITE 3 RETAS E VERIFIQUE SE PODEM FORMAR UM TRIANGULO!{}\n\n'.format('\033[33m', '\033[m'))

r1 = int(input('Medida 1: '))
r2 = int(input('Medida 2: '))
r3 = int(input('Medida 3: '))

if r1+r2>r3 and r2+r3>r1 and r1+r3>r2:
    print('\n\nas medidas {}, {} e {}: {}podem formar um triangulo!{}'.format(r1, r2, r3, '\033[35m', '\033[m'))

    if r1 == r2 and r1 == r3:
        print('Tipo do triangulo: {}EQUILÁTERO{}'.format('\033[36m', '\033[m'))
    elif r1 == r2 and r2 != r3:
        print('Tipo do triangulo: {}ISÓSCELES{}'.format('\033[34m', '\033[m'))
    elif r1 == r3 and r2 != r1:
        print('Tipo do triangulo: {}ISÓSCELES{}'.format('\033[34m', '\033[m'))
    elif r2 == r3 and r2 != r1:
        print('Tipo do triangulo: {}ISÓSCELES{}'.format('\033[34m', '\033[m'))
    else:
        print('Tipo do triangulo: {}ESCALENO{}'.format('\033[32m', '\033[m'))

else:
    print('as medidas {}, {} e {}: {}NÃO podem formar um triangulo!{}'.format(r1, r2, r3, '\033[31m', '\033[m'))
