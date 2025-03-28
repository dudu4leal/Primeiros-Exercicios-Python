#Programa que lê o ano de nascimento de sete pessoas. No final, mostra quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.

import datetime


hoje = datetime.date.today()
anoAtual = hoje.year
idades = []
countMaior = 0
countMenor = 0

for i in range(0,7):
    anoNascimento = int(input('digite o ano de nascimento da {}° pessoa: '.format(i+1)))

    idade = anoAtual - anoNascimento
    idades.append(idade)

for j in range(0,7):
    print('a idade da {}° pessoa é: {}'.format(j+1, idades[j]))

    if idades[j] >=18:
        print('ela já atingiu a maioridade.')
        countMaior+=1

    else:
        print('ela não atingiu a maioridade.')
        countMenor+=1

print('{} pessoa(s) já atingiu/atingiram a maioridade\n'
        'e {} pessoa(s) não atingiram a maioridade ainda.'.format(countMaior, countMenor))