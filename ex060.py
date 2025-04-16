#Programa que lê um número qualquer e mostra o seu fatorial

from math import factorial

numero = int(input('digite o numero: '))
fatorial = factorial(numero)
count = numero

print('calculando {}! = '.format(numero), end='')
while count > 0:
    print('{}'.format(count), end='')
    print(' x ' if count > 1 else ' = ', end='')
    count -= 1

print(fatorial)