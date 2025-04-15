#programa que lê o nome, idade e sexo de 4 pessoas. No final do programa, mostra: a média de idade do grupo, qual é o nome do homem mais velho e 
#quantas mulheres têm menos de 20 anos.

nomes = []
idades = []
sexos = []

for i in range (0, 4):
    nome = input('digite o nome da {}ª pessoa: '.format(i+1))  
    nomes.append(nome)

    idade = int(input('digite a idade da {}ª pessoa: '.format(i+1)))
    idades.append(idade)

    sexo = input('qual o sexo da {}ª pessoa (H para homem e M para mulher): '.format(i+1))
    sexo = sexo.upper()
    sexos.append(sexo)

somaIdades = 0.0

for i in range (0, len(nomes)):
    
    somaIdades += idades[i]

mediaIdades = somaIdades/4
print('a média das idades é {}'.format(mediaIdades))

maiorIdade = 0

for i in range(0, 4):
    if sexos[i] == 'H':
        if idades[i] > maiorIdade:
            maiorIdade = idades[i]

for i in range(0, 4):
    if sexos[i] == 'H':
        if idades[i] == maiorIdade:
            print('o homem mais velho é o {}'.format(nomes[i]))

countM = 0
for i in range(0, 4):
    if sexos[i] == 'M':
        if idades[i] < 20:
            countM+=1

print('{} mulher(es) tem menos de 20 anos'.format(countM))