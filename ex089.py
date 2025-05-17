#programa que lê nome e duas notas de vários alunos e guarda tudo em uma lista composta. No final, mostra um boletim 
# contendo a média de cada um e permite que o usuário possa mostrar as notas de cada aluno individualmente.

boletimTurma = []
condicao = 'S'
count = 0

while condicao == 'S':

    boletimTurma.append(list())

    nome = input(f'digite o nome do {count+1}º aluno(a): ')
    boletimTurma[count].append(nome)

    nota1 = float(input(f'digite a 1ª nota do(a) {nome}: '))
    boletimTurma[count].append(nota1)
    
    nota2 = float(input(f'digite a 2ª nota do(a) {nome}: '))
    boletimTurma[count].append(nota2)

    media = (nota1+nota2)/2
    boletimTurma[count].append(media)

    condicao = input('deseja inserir as notas de mais um aluno? [S/N]: ').strip().upper()
    while condicao != 'S' and condicao != 'N':
        condicao = input('condicao inválida.  Digite novamente [S/N]: ').strip().upper()

    count+=1


print('='*60)
print('BOLETIM: ')
print('='*60)

print('-'*60)
for i in range(0, count):

    print(f'Aluno: {boletimTurma[i][0]}')
    print(f'Média: {boletimTurma[i][3]:.1f}')
    print('-'*60)


for i in range (0, count):

    resposta = input(f'Deseja mostrar as notas individuais do(a) {boletimTurma[i][0]}? [S/N]: ').strip().upper()
    while resposta != 'S' and resposta != 'N':
        resposta = input('resposta inválida. Digite novamente [S/N]: ').strip().upper()

    print('='*60)
    if resposta == 'S':
        print(f'Nota 1: {boletimTurma[i][1]}')
        print(f'Nota 2: {boletimTurma[i][2]}')
    print('='*60)
