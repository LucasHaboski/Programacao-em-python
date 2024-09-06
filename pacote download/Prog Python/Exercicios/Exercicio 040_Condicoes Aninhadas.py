# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('='*40)
print('{}VERIFICADOR DE MÉDIA!{}'.format('\033[35m','\033[m'))
print('='*40)

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua seguunda nota: '))

m = (n1 + n2) / 2

if m >= 7.0:
    print('\nPARABENS VOCE PASSOU!!\nSTATUS: {}APROVADO{}\nMÉDIA: {}{:.1f}{}'.format('\033[32m', '\033[m', '\033[32m', m, '\033[m'))
elif m >= 5.0 and m < 7.0:
    print('\nFIQUE ATENTO, ESTUDE BASTANTE!\nSTATUS: {}RECUPERAÇÃO{}\nMÉDIA: {}{:.1f}{}'.format('\033[33m', '\033[m', '\033[33m', m, '\033[m'))
else:
    print('\nINFELIZMENTE, NÃO FOI DESSA VEZ!\nSTATUS: {}REPROVADO{}\nMÉDIA: {}{:.1f}{}'.format('\033[31m', '\033[m', '\033[31m', m, '\033[m'))