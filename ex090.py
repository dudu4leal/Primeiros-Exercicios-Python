#programa que lê nome e média de um aluno, guardando também a situação em um dicionário. No final, mostra o conteúdo da estrutura na tela.

dicionario = {}

dicionario['nome'] = str(input('Digite o nome do(a) aluno(a): ')).capitalize()

media = float(input('Digite a média do(a) aluno(a): '))

dicionario['media'] = media

if media >= 6:
    
    dicionario['situação'] = 'Aprovado'

elif media >= 4.5 and media < 6:

    dicionario['situação'] = 'em Recuperação'

else:
    dicionario['situação'] = 'Reprovado'


print(f'O {dicionario["nome"]} teve média {dicionario["media"]} e está {dicionario["situação"]}')
