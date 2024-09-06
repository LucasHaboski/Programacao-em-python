#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

print('='*60)
print('Descubra se 3 medidas aleatórias podem formar um triangulo!')
print('='*60)

a = int(input('Digite a primeira medida: '))
b = int(input('Digite a segunda medida: '))
c = int(input('Digite a terceira medida: '))

if a+b>c and a+c>b and b+c>a: #regra para formação de um triangulo
    print('\nCom as medidas {}, {} e {}:\nÉ possivel formar um triangulo!'.format(a,b,c))
else:
    print('\nCom as medidas {}, {} e {}:\nNÃO é possivel formar um triangulo;-;'.format(a,b,c))
