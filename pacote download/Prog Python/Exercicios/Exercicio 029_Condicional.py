#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h
#Mostre uma mensagem dizendo que ele foi multado, a multa vai custar R$7,00 por cada Km acima do limite

print('='*40)
print('Programa Velocimetro, verificador de multa')
print('='*40)

velo = int(input('\nDigite a velocidade o carro passou no radar: '))

if velo > 80:
    preco = (velo - 80) * 7
    print('\nVoce ultrapassou o limite de velocidade e foi multado!\nA multa ficara no valor de: R${},00'.format(preco))
else:
    print('\nVoce andou dentro do limite permitido de velocidade, Parabens!!!')
