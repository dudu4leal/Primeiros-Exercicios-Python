#programa que joga par ou ímpar com o computador. O jogo será interrompido quando o jogador perder, mostrando o total de vitórias 
#consecutivas que ele conquistou no final do jogo.

import os
from random import *

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-' * 30)

count = 0

while True:
    
    parOuImparJ = input('par ou ímpar [P/I]: ')
    parOuImparJ = parOuImparJ.upper()
    while parOuImparJ != 'P' and parOuImparJ != 'I':
        parOuImparJ = input('par ou ímpar [P/I]: ')
        parOuImparJ = parOuImparJ.upper()


    if parOuImparJ == 'P':
        parOuImparC = 'I'

    elif parOuImparJ == 'I':
        parOuImparC = 'P'


    numeroJogador = int(input('jogue um número(0 até 10): '))
    while numeroJogador < 0 or numeroJogador > 10:
        numeroJogador = int(input('jogue um número (0 até 10): '))
    
    numeroComputador = randint(0, 10)

    somaJogadas = numeroJogador + numeroComputador

    if somaJogadas % 2 == 0:
        
        resultadoDoJogo = 'P'
        print('-' * 30)
        print(f'você jogou {numeroJogador} e o computador jogou {numeroComputador}. Total de {somaJogadas} deu par')
        print('-' * 30)

    elif somaJogadas % 2 != 0:

        resultadoDoJogo = 'I'
        print('-' * 30)
        print(f'você jogou {numeroJogador} e o computador jogou {numeroComputador}. Total de {somaJogadas} deu ímpar')
        print('-' * 30)

    if parOuImparJ == resultadoDoJogo:
        print('VOCÊ VENCEU!')
        print('-' * 30)
        count += 1
    elif parOuImparJ != resultadoDoJogo:
        print('VOCÊ PERDEU!')
        print('-' * 30)
        break

print (f'GAME OVER! Você venceu {count} vezes.')

os.system("pause")