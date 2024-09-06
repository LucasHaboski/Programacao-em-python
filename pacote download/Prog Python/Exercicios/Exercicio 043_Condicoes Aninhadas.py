# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25.0: Peso Ideal
# - Entre 25.0 e 30.0: Sobrepeso
# - Entre 30.0 e 40.0: Obesidade
# - Acima de 40.0: Obersidade Mórbida

from math import pow  # bibloteca potencia

#Cabeçalho
print('='*15)
print('{}CALCULO DE IMC!{}'.format('\033[36m','\033[m'))
print('='*15)    

#Input de dados
peso = float(input('\nDigite o seu Peso em Kg: '))
altura = float(input('Digite a sua altura em Metros: '))

#Calculo I.M.C
imc = peso / pow(altura, 2)

#Condiçoes + print
if imc < 18.5:
    print('I.M.C: {}{:.1f}{}\nStatus: {}Abaixo do peso{}'.format('\033[33m', imc, '\033[m', '\033[33m','\033[m'))        # Amarelo
elif imc < 25.0:
    print('I.M.C: {}{:.1f}{}\nStatus: {}Peso ideal{}'.format('\033[32m', imc, '\033[m', '\033[32m','\033[m'))            # Verde
elif imc < 30.0:
    print('I.M.C: {}{:.1f}{}\nStatus: {}Sobrepeso{}'.format('\033[34m', imc, '\033[m', '\033[34m','\033[m'))             # Azul
elif imc < 40.0:
    print('I.M.C: {}{:.1f}{}\nStatus: {}Obesidade{}'.format('\033[35m', imc, '\033[m', '\033[35m','\033[m'))             # Roxo
else:
    print('I.M.C: {}{:.1f}{}\nStatus: {}Obersidade Mórbida{}'.format('\033[31m', imc, '\033[m', '\033[31m','\033[m'))    # Vermelho