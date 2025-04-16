#Melhorando o jogo do DESAFIO 28 onde o computador “pensa” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import *

numeroMisterioso = randint(0, 11)

print('tente adivinhar no número que estou pensando. Dica: ele está entre 0 e 10')

numeroJogador = int(input('tente um número: '))

count = 0

while numeroJogador != numeroMisterioso:
    count +=1
    
    if numeroJogador < 0 or numeroJogador > 10:
        numeroJogador = int(input('ops... esse número não está entre 0 e 10. Tente novamente.\n'))
    
    else:
        numeroJogador = int(input('haha, você errou! Tente novamente!\n'))
    

print('parabéns! Você acertou!!! Precisou de {} tentativas e o número era: {}'.format(count+1, numeroMisterioso))