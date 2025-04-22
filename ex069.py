#programa que lê a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa pergunta se o usuário 
#quer ou não continuar. No final, mostra: quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados, 
#quantas mulheres tem menos de 20 anos.

vetIdade = []
vetSexo = []
count = 0

while True:
    
    idade = -1
    while idade < 0:
        idade = int(input('digite a idade da {}ª pessoa: '.format(count+1)))
    vetIdade.append(idade)

    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = input('digite o sexo da {}ª pessoa[M/F]: '.format(count+1)).strip().upper()
    vetSexo.append(sexo)

    count += 1

    condicao = ''
    while condicao != 'S' and condicao != 'N':
        condicao = input('deseja continuar? [S/N]: ')
        condicao = condicao.strip().upper()

    if condicao == 'N':
        break

countMI = 0

for i in range (0, len(vetIdade)):

    if vetIdade[i] >= 18:
        countMI += 1

countHomens = 0

for i in range(0, len(vetSexo)):

    if vetSexo[i] == 'M':
        countHomens += 1

countMMV = 0

for i in range(0, len(vetSexo)):

    if vetSexo[i] == 'F':
        if vetIdade[i] < 20:
            countMMV += 1


print(f'{countMI} pessoa(s) são maiores de idade')
print(f'{countHomens} homen(s) foram cadastrados')
print(f'{countMMV} mulher(es) tem menos de 20 anos')

