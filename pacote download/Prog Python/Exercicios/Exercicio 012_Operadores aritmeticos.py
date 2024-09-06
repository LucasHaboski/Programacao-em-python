#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

val = float(input('Digite o valor do produto: R$'))

print("Aplicando o desconto de 5% o seu produto fica custando: R${:.2f}".format(val*0.95))