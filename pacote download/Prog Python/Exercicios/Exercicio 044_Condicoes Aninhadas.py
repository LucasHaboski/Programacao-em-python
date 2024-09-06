# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro / cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
 
#Cabeçalho
print('='*26)
print('{}MERCADIIINHO BIG BOOOOM!{}'.format('\033[36m','\033[m'))
print('='*26)

#Input dados
preco = float(input('\nDigite o preço original do produto: '))

#Print switch case
print('Qual a forma de pagamento?\n1- {}Dinheiro / Cheque{}\n2- {}À vista no cartão{}\n3- {}2x No cartão{}\n4- {}3x ou Mais no Cartão{}'.format('\033[32m','\033[m','\033[33m','\033[m','\033[34m','\033[m','\033[36m','\033[m'))

#input case
esc = int(input('Digite a forma de pagamento: '))

#Escolhas + print
if esc == 1:
    print('\n\nNessa forma de pagamento conseguimos 10% de desconto\nValor final: {}R${:.2f}{}'.format('\033[32m', preco * 0.9,'\033[m'))
elif esc == 2:
    print('\n\nNessa forma de pagamento conseguimos 5% de desconto\nValor final: {}R${:.2f}{}'.format('\033[33m', preco * 0.95,'\033[m'))
elif esc == 3:
    print('\n\nNessa forma de pagamento não existe desconto\nValor final: {}R${:.2f}{}'.format('\033[34m', preco ,'\033[m'))
elif esc == 4:
    print('\n\nNessa forma de pagamento exite 20% de juros no valor total\nValor final: {}R${:.2f}{}'.format('\033[36m', preco * 1.2,'\033[m'))
else: 
    print('{}VOCE DIGITOU UM VALOR INVALIDO! TENTE NOVAMENTE!{}'.format('\033[31m','\033[m'))