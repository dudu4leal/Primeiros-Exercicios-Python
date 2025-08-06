#Programa que lê um número real e mostra sua porção inteira

import math 

numeroReal = float(input('Digite um número real: '))

print('Número real: {}\nParte inteira: {}'.format(numeroReal, math.trunc(numeroReal)))