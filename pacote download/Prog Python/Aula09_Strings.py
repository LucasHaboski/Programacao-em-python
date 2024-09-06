frase = input('Digite alguma coisa: ')

print(frase[9:21:2]) #print a partir do indice 9 até 21 pulando 2
print(frase[:21]) #print do 0 a 21
print(frase[9:]) #print do 9 a 21
print(frase[9::3]) #print do 9 a 21 pulando 3

print('Tamanho da string: {}'.format(len(frase))) #tamanho da string
print('Vezes que "e" aparece: {}'.format(frase.count('e',0,18))) #ocorrencia de caracter na string
print('Encontrar repartição deo, começa: {}'.format(frase.find('deo'))) #indice onde inicia a parte procurada
print('Python' in frase) #resposta True ou False para pesquisa
print(frase.replace('Python', 'Sacoleta')) #Trocar (não na lista) o elemento da string
print(frase.upper()) #Tudo maiusculo
print(frase.lower()) #Tudo minusculo
print(frase.capitalize()) #Primeira letra da Frase em Maiusculo
print(frase.title()) #Primeira letra de todas as palavras em Maiusculo
print(frase.split()) #Dividir a String separando pelos espaços
print('-'.join(frase)) #junta-las utilizando algum caractere

frase_2 = '   Testando partedois  '

print(frase_2.strip()) #Corta espaços desnecessarios
print(frase_2.rstrip()) #Corta espaços da direita
print(frase_2.lstrip()) #Corta espaços da esquerda

print("""\n\nComece agora: não espere pelo momento perfeito, comece hoje, com o que tem.
Sonhe grande: se seus sonhos não dão um frio na barriga, talvez ainda não sejam grandes o bastante.
Ação diária: pequenos passos diários constroem grandes realizações.
Confie: a autoconfiança é o primeiro passo para grandes feitos.\n""") #Printando frase grande

print(f'Teste de fstrings: {frase}') #fstrings

nome = 'Lucas'
idade = 20

print(f'O {nome} tem {idade} anos!')