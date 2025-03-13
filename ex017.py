#Programa que lê o valor do cateto oposto e do cateto adjacente do triangulo retangulo e informa o valor da hipotenusa

import math

catetoOposto = float(input('Cateto oposto = '))
catetoAdjacente = float(input('Cateto ajacente = '))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('Hipotenusa = {:.2f}'.format(hipotenusa))