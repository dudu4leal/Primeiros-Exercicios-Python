#programa onde o usuário pode digitar vários valores numéricos e cadastra-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []
count = 0
condicao = 'S'
    
while condicao == 'S':
    
    n = int(input(f'Digite o {count + 1}º número: '))

    while True:
        if n in numeros:
            n = int(input('Este número já está na lista. Digite outro valor: '))
        else:
            numeros.append(n)
            break

    condicao = input('Deseja cadastrar mais um número? [S/N]: ').strip().upper()
    while condicao != 'S' and condicao != 'N':
        condicao = input('condição inválida. Digite novamente[S/N]: ').strip().upper()

    count+=1

numeros.sort()
print(f'Lista digitada em ordem crescente: {numeros}')

