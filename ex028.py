#O computador vai me pensar num número de 0 até 5 e o usuário vai tentar adivinhar
#Caso o usuário acerte o programa diz q ele venceu, se não ele diz que perdeu

from random import *

numeroMisterioso = randint(0, 6)

numeroUsuario = int(input('opções: 1, 2, 3, 4 ,5\ndigite seu palpite: '))

if numeroUsuario == numeroMisterioso:
    print('você venceu!')
else:
    print('você perdeu... ):')
    print('o número era: {}'.format(numeroMisterioso))