#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (U$1,00 = R$3,27)

din = float(input('Digite quantos Reais tem na conta: R$'))

print('\nCom R${:.2f} voce poderá comprar U${:.2f}!!!\n'.format(din, din/3.27))