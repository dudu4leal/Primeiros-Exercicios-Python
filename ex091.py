#programa onde 4 jogadores jogam um dado e tem resultados aleatórios. Guarda esses resultados em um dicionário em Python. No final, coloca esse dicionário 
#em ordem, sabendo que o vencedor tirou o maior número no dado.

import random
from time import sleep
from operator import itemgetter


jogadores = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6), 'jogador3': random.randint(1, 6), 'jogador4': random.randint(1, 6)}

print('Valores sorteados: ')
sleep(1)
for i, j in jogadores.items():
    print(f'{i} tirou {j} no dado')
    sleep(1)

print('-='*30)

print('<< RANKING DOS JOGADORES >>')

jogadoresOrdenados = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

posicao = 1
for k, v in jogadoresOrdenados.items():
    sleep(1)
    print(f'{posicao}º lugar: {k} com {v} pontos')
    posicao += 1    
