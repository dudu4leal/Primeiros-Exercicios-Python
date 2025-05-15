#programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão conter apenas os valores pares e os valores ímpares
#digitados, respectivamente. Ao final, mostra o conteúdo das três listas geradas.

listaGeral = []
condicao = 'S'
count = 1

while condicao == 'S':

    listaGeral.append(int(input(f'digite o {count}º número: ')))

    condicao = input('deseja ler mais um número? [S/N]: ').strip().upper()
    while condicao != 'S' and condicao != 'N': 
        condicao = input('condicao inválida. Digite novamente: [S/N]: ').strip().upper()

    count +=1


listaPares = []
listaImpares = []


for i in range(0, len(listaGeral)):
    
    if listaGeral[i] % 2 == 0:
        
        listaPares.append(listaGeral[i])

    else:

        listaImpares.append(listaGeral[i])


print('='*30)

print(f'Lista original: {listaGeral}')
print('-'*30)
print(f'Lista apenas com números pares: {listaPares}')
print('-'*30)
print(f'Lista apenas com números impares: {listaImpares}')

print('='*30)
