#Programa que lê um angulo qualquer e mostra seu seno, cosseno e sua tangente

import math

angulo = int(input('Angulo = '))

anguloRad = math.radians(angulo)

seno = math.sin(anguloRad)
cosseno = math.cos(anguloRad)

print('seno = {:.2f}\ncosseno = {:.2f}'.format(seno, cosseno))

if math.isclose(cosseno, 0, abs_tol=1e-9):
    print('tangente indefinida')

else:
    tangente = math.tan(anguloRad)
    print('tangente = {:.2f}'.format(tangente))