#Aprimorando o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
import sys

jogador = dict()
golsPorPartidas = list()
lisaDeJogadores = list()
condicao = 'S'


count = 1
while condicao == 'S':

    jogador['Nome'] = str(input(f'Digite o nome do {count}º jogador: '))
    
    totalPartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for i in range(0, totalPartidas):
        golsPorPartidas.append(int(input(f'Quantos gols {jogador["Nome"]} fez na {i+1}ª partida? ')))

    jogador['gols'] = golsPorPartidas[:]

    jogador['Total de Gols'] = sum(golsPorPartidas)

    golsPorPartidas.clear()

    lisaDeJogadores.append(jogador.copy())

    count+=1

    condicao = str(input('Deseja cadastrar os dados de mais um jogador? [S/N]: ')).strip().upper()
    while condicao != 'S' and condicao != 'N':
        condicao = str(input('Condição inválida. Digite novamente[S/N]: ')).strip().upper()

print('='*45)
print('Cód. do Atleta     Gols p/ jogo     Total de gols')
print('-'*45)


for i in range(0, len(lisaDeJogadores)):
    print(f'{i} {lisaDeJogadores[i]["Nome"]}', end='   ')
    print(f'{lisaDeJogadores[i]['gols']}', end='   ')
    print(f'{lisaDeJogadores[i]['Total de Gols']}')


codigoAtleta = int(input('Mostrar dados de qual jogador? (999 pra sair)'))
while codigoAtleta < 0 or codigoAtleta >= len(lisaDeJogadores):
    codigoAtleta = int(input('Codigo inválido. Digite novamente: '))
    if codigoAtleta == 999:
        sys.exit(0)


while True:

    print(f'Levantamento do jogador {lisaDeJogadores[codigoAtleta]['Nome']}')
    
    for i, gols in enumerate (lisaDeJogadores[codigoAtleta]['gols']):
        print(f'No jogo {i+1} fez {gols} gols')      

    codigoAtleta = int(input('deseja ver o levantamento de mais algum jogador? (999 pra encerrar)'))

    if codigoAtleta == 999:
        
        break
    
    else:
        while codigoAtleta < 0 or codigoAtleta >= len(lisaDeJogadores):
            codigoAtleta = int(input('Codigo inválido. Digite novamente: '))

            if codigoAtleta == 999:
                sys.exit(0)
