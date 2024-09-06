idade = int(input('Quantos anos você tem? '))

#Metodo Convencional

if idade < 18:
    print('Você é menor de idade')
else: 
    print('Você é maior de idade')

#Método Simplificado

print('Você é menor de idade' if idade < 18 else 'Você é maior de idade')

print('teste')

print('====FIM====')
