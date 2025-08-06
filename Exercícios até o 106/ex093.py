#programa que gerencia o aproveitamento de um jogador de futebol. O programa lê o nome do jogador e quantas partidas ele jogou. 
#Depois lê a quantidade de gols feitos em cada partida. No final, tudo isso é guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


gols = []
totalGols = 0


nome = str(input('Nome do jogador: '))
totalpartidas = int(input(f'Quantas partidas {nome} jogou? '))

for i in range (0, totalpartidas):

    gol = int(input(f'Quantos gols {nome} fez na {i+1}ª partida? '))
    gols.append(gol)

    totalGols += gol

dadosPartida = {'Nome do jogador' : nome, 'G/P': gols, 'Total de gols': totalGols}

print('='*45)

print(f'Nome do jogador: {dadosPartida["Nome do jogador"]}')

print('='*45)

count = 1
for i in dadosPartida['G/P']:
    
    print(f'na {count}ª partida o jogador {dadosPartida["Nome do jogador"]} marcou {dadosPartida["G/P"][i]} gols')

    count +=1

print('='*45)

print(f'O total de gols foi {dadosPartida["Total de gols"]}')

print('='*45)

#print(f'Nome do jogador: {nome}')

#for i in range (0, len(gols)):

#    print(f'Na {i+1}ª partida {nome} marcou {gols[i]} gols')

#print(f'Seu total de gols foi {totalGols}')
