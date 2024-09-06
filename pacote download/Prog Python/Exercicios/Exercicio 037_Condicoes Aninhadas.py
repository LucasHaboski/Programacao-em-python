#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO
# - 1 para binário (%)
# - 2 para octal ()
# - 3 para hexadecimal

num = int(input('Digite um numero e escolha qual {}BASE DE CONVERSÃO{} deseja: '.format('\033[36m', '\033[m')))

esc = int(input('Qual base deseja converter?\n1 - {}BINÁRIO{}\n2 - {}OCTAL{}\n3 - {}HEXADECIMAL{}\n'.format('\033[32m','\033[m','\033[35m','\033[m','\033[31m','\033[m')))

if esc == 1:
    print('O numero {} convertido para {}BINÁRIO{} é: {}{}{}'.format(num,'\033[32m','\033[m','\033[32m', bin(num)[2:],'\033[m'))
elif esc == 2:
    print('O numero {} convertido para {}OCTAL{} é: {}{}{}'.format(num,'\033[35m','\033[m','\033[35m', oct(num)[2:],'\033[m'))
elif esc == 3:
    print('O numero {} convertido para {}HEXADECIMAL{} é: {}{}{}'.format(num,'\033[31m','\033[m','\033[31m', hex(num)[2:],'\033[m'))
else:
    print('{}VOCÊ DIGITOU UM NUMERO INVALIDO, TENTE NOVAMENTE!{}'.format('\033[31m','\033[m')) 