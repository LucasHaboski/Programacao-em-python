#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

dist = int(input('Digite qual a distância da sua viagem: '))

if dist <= 200:
    print('A passagem ficara no valor de: R${:.2f}'.format(dist*0.5))
else:
    print('A passagem ficara no valor de: R${:.2f}'.format(dist*.45))