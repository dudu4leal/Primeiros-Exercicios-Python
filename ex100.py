#programa que tem uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
#A primeira função sorteia 5 números e vai colocá-los dentro da lista e a segunda função mostra a soma entre todos os valores pares sorteados pela função anterior.

import random
from time import sleep

def sorteia(lista):

    print('Sortando a lista...')
    for i in range(0, 5):

        lista.append(random.randint(1, 10))
        print(f'{lista[i]} ', end='', flush = True)
        sleep(0.3)

    print('Pronto!')

def somaPar(lista):

    soma = 0

    for i in range(0, len(lista)):

        if lista[i] % 2 == 0:
           soma = soma + lista[i]
    
    print(f'Soma dos valores pares é: {soma}')


numeros = []

sorteia(numeros)
somaPar(numeros)
