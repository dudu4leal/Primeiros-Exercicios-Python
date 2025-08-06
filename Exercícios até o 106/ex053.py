#Programa que lê uma frase qualquer e diz se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite  Frase: ')
frase = frase.upper()

fraseForm = frase.replace(' ', '')

fraseInv = ''.join(reversed(fraseForm))
#print(fraseInv)

print('{} invertido é: {}'.format(fraseForm, fraseInv))
if fraseInv == fraseForm:
    print('temos um palíndromo!')
else:
    print('não é um palíndromo.')
