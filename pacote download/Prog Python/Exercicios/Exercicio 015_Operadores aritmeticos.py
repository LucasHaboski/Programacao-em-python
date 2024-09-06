#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

print('='*40)
print('BEM VINDO A LOCADORA AUTOMOVEIS GUARANA')
print('='*40)

p_d = int(input('\nQuantos dias o carro foi alugado? ')) * 60
p_km = float(input('Qual foi a distancia (Km) percorrida pelo carro alugado? ')) * 0.15

print('\nO valor a pagar por {:.0f} dias com o carro vai ser: R${:.2f}'.format(p_d / 60, p_d+p_km))
