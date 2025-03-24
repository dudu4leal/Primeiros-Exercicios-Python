#Programa que faz o computador jogar Jokenpô com você

from random import *
from time import sleep

print(
        '[0] pedra\n'
        '[1] papel\n'
        '[2] tesoura\n'
                        )

itens = ('pedra', 'papel', 'tesoura')

numeroJogador = int(input('qual é a sua jogada? '))
numeroComputador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('='*11)
print('jogador escolheu: {}'.format(itens[numeroJogador]))
print('jogada do computador: {}'.format(itens[numeroComputador]))
print('='*11)

#inicio da condição de empate
if numeroJogador == numeroComputador:
    print('empate.')
#final da condição de empate

#inicio das condições pedra e papel
elif numeroJogador == 0 and numeroComputador == 1:
    print('computador venceu!') 

elif numeroJogador == 1 and numeroComputador == 0:
    print('você venceu!')
#final das condições pedra e papel

#inicio das condições papel e tesoura
elif numeroComputador == 1 and numeroJogador == 2:
    print('você venceu!')

elif numeroComputador == 2 and numeroJogador == 1:
    print('computador venceu!')
#final das condições papel e tesoura

#inicio das condições pedra e tesoura
elif numeroComputador == 0 and numeroJogador == 2:
    print('computador venceu!')

elif numeroComputador == 2 and numeroJogador == 0:
    print('você venceu!')
#final das condições pedra e tesoura

else:
    print('algo deu errado. Tente novamente\nerro 400')