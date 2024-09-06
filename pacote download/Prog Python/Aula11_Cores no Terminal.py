a = 5
b = 9

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b)) #primeira forma, colorindo no print

print('E a soma entre eles é {}{}{} !!'.format('\033[35m', a+b, '\033[m')) #segunda forma, colorindo no format

#terceira forma, criando uma lista de cores e colorindo pelo format

cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m', 
         'azul escuro':'\033[34m', 
         'roxo':'\033[35m', 
         'azul claro': '\033[36m',
         'cinza': '\033[37m'}

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

print('Numeros digitados {}{}{} e {}{}{} !'.format(cores['verde'], n1, cores['limpa'], cores['azul claro'], n2, cores['limpa']))
print('Soma entre eles: {}{}{}!! \n\n'.format(cores['roxo'], n1+n2, cores['limpa']))

print('{}Vermelho{}'.format(cores['vermelho'], cores['limpa']))
print('{}Verde{}'.format(cores['verde'], cores['limpa']))
print('{}Amarelo{}'.format(cores['amarelo'], cores['limpa']))
print('{}Azul Claro{}'.format(cores['azul claro'], cores['limpa']))
print('{}Roxo{}'.format(cores['roxo'], cores['limpa']))
print('{}Azul escuro{}'.format(cores['azul escuro'], cores['limpa']))
print('{}Cinza{}'.format(cores['cinza'], cores['limpa']))
