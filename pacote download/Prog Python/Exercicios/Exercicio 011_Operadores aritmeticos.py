#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, 
# pinta uma area de 2m^2

lar = float(input('Escreva qual a largura da parede: '))
alt = float(input('Escreva qual a altura da parede: '))

area = lar * alt

print('A area da parede é {:.0f} m2\nSera necessario ultilizar {:.0f} litros de tinta'.format(area, area/2))