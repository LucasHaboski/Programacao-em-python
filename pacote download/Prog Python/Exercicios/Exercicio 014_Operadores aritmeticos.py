#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

grau = float(input('Digite a temperatura em °C: '))

print('\nA temperatura convertida é: {:.2f}°F'.format(grau*1.8+32))