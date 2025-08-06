#programa que lê nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostra: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

listNomes = []
listSexos = []
listIdades = []

listGeral = []

count = 1
condicao = 'S'
while condicao == 'S':

    nome = str(input(f'Digite o nome da {count}ª pessoa: '))
    listNomes.append(nome)

    idade = int(input(f'Digite a idade da {count}ª pessoa: '))
    listIdades.append(idade)

    sexo = str(input(f'Digite o sexo da {count}ª pesssoa[M/F]: ')).strip().upper()
    
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('sexo inválido. Digite novamente[M/F]: ')).strip().upper()
    
    listSexos.append(sexo)

    condicao = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().upper()
    
    while condicao != 'S' and condicao != 'N':
        condicao = str(input('Condição inválida. Digite novamente [S/N]:')).strip().upper()

    if condicao == 'S':
        count+=1


dictNomes = {'Nomes': listNomes}
dictIdades = {'Idades': listIdades}
dictSexos = {'Sexos': listSexos}

listGeral = [dictNomes, dictIdades, dictSexos]


somaIdades = 0
for i in range(0, len(listIdades)):
    somaIdades += listIdades[i]

mediaIdades = somaIdades/len(listIdades)


listMulheres = []
for i in range(0, len(listSexos)):
    
    if listSexos[i] == 'F':
        listMulheres.append(listNomes[i])


listMaisVelhos = []
for i in range (0, len(listIdades)):
    
    if listIdades[i] > mediaIdades:
        listMaisVelhos.append(listNomes[i])


print(f'Foram cadastradas {count} pessoas')
print(f'A média de idades foi {mediaIdades:.1f}')
print(f'As mulheres cadastradas foram {listMulheres}')
print(f'As pessoas com idade acima da média foram {listMaisVelhos}')
