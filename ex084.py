#programa que lê o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostra:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

lista = []
pessoa = []
condicao = 'S'
count = 0


while condicao == 'S':

    pessoa.append(input(f'Digite do nome da {count+1}ª pessoa: '))
    pessoa.append(float(input(f'Digite o peso da {count+1}ª pessoa: ')))
    
    lista.append(pessoa[:])

    pessoa.clear()

    count += 1

    condicao = input('Deseja cadastrar mais uma pessoa? [S/N]: ').strip().upper()
    while condicao != 'S' and condicao != 'N':
        condicao = input('Resposta inválida. Digite novamente [S/N]: ').strip().upper()


maiorPeso = 0
menorPeso = 0
pessoasMaisPesadas = []
pessoasMaisLeves = []


for i in range(0, len(lista)):
    
    if i == 0:
        
        maiorPeso = lista[i][1]
        pessoasMaisPesadas.append(lista[i][0])
        menorPeso = lista[i][1]
        pessoasMaisLeves.append(lista[i][0])

    else:

        if lista[i][1] > maiorPeso:
        
            maiorPeso = lista[i][1]
            pessoasMaisPesadas.clear()
            pessoasMaisPesadas.append(lista[i][0])

        elif lista[i][1] == maiorPeso:

            pessoasMaisPesadas.append(lista[i][0])
        

        elif lista[i][1] < menorPeso:
        
            menorPeso = lista[i][1]
            pessoasMaisLeves.clear()
            pessoasMaisLeves.append(lista[i][0])

        elif lista[i][1] == menorPeso:

            pessoasMaisLeves.append(lista[i][0])

stringPessoasMaisPesadas = ', '.join(pessoasMaisPesadas)
stringPessoasMaisLeves = ', '.join(pessoasMaisLeves)


print('='*60)

print(f'Foram cadastradas {count} pessoas.')
print(f'O maior peso registrado foi {maiorPeso}kg na(s) pessoa(s): {stringPessoasMaisPesadas}')
print(f'O menor peso registrado foi {menorPeso}kg na(s) pessoa(s): {stringPessoasMaisLeves}')

print('='*60)
