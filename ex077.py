#programa que tem uma tupla com várias palavras (sem uso de acentos). Depois disso, mostra, para cada palavra, 
#quais são as suas vogais.

def mostrar_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_na_palavra = ''

    for i in palavra:
        if i in vogais:
            vogais_na_palavra += i

    print(vogais_na_palavra)



tupla_palavras = ('relampago', 'girassol', 'montanha', 'espelho', 'labirinto')

for i in range (0, len(tupla_palavras)):

    mostrar_vogais(tupla_palavras[i])