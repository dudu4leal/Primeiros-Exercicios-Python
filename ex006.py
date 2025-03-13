#Algoritimo que lê um número e mostra seu dobro, seu triplo e sua raiz quadrada
import math


n = int(input('Digite um número: '))

print('Dobro = {}\nTriplo = {}\nRaiz quadrada = {} '.format(n*2, n*3, math.sqrt(n)))