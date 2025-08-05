#programa que tem uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
#O programa deve ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome = '<desconhecido>', gols= 0):

    return f'O jogador {nome} marcou {gols} gol(s).'


nome = str(input('Qual o nome do jogador?\n'))
gols = str(input('Quantos gols ele marcou?\n'))


if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0


if nome.strip() == '':
    print(ficha(gols=gols))

else:
    print(ficha(nome, gols))
