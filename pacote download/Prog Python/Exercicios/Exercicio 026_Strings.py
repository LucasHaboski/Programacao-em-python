#Faça um programa que leia uma frase pelo teclado e mostre: 
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite um frase: ')).strip()

frase_au = frase.upper()

print('A letra "A" aparece: {} vezes!'.format(frase_au.count('A')))
print('A letra "A" aparece a primeira vez no indice [{}]!'.format(frase_au.find('A')+1))
print('A letra "A" aparece a ultima vez no indice [{}]!'.format(frase.rfind('A')+1))
