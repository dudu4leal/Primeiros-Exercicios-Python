#Programa que lê uma frase e diz:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece a última vez

frase = input('Digite a frase: ')

frase = frase.upper()


if frase.find('A') == -1 and frase.rfind('A') == -1:
    print('A frase não possui a letra "A"')
else:
    print('a letra "A" aparece {} vez(es)'.format(frase.count('A')))
    print('a letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')))
    print('a letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')))