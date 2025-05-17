#programa que ajuda um jogador da MEGA SENA a criar palpites.O programa pergunta quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

qtdJogos = int(input('quanto jogos quer jogar? '))
jogos = []


for i in range(0, qtdJogos):
    jogos.append(list())


for i in range (0, qtdJogos):
    for j in range (0, 6):
        jogos[i].append(randint(0, 61))


print('='*60)

for i in range(0, qtdJogos):
    print(f'Números pro {i+1}º jogo: {jogos[i]}')

print('='*60)
