#programa que lê o nome e o preço de vários produtos. O programa deve perguntar se o usuário vai continuar ou não.
#No final, mostra: A) qual é o total gasto na compra, B) quantos produtos custam mais de R$1000, 
#C) qual é o nome do produto mais barato.

vetProdutos = []
vetPrecos = []
count = 0

while True:

    produto = input(f'digite o nome do {count+1}º produto: ').strip().capitalize()
    vetProdutos.append(produto)

    preco = -1
    while preco < 0: 
        preco = float(input(f'digite o valor do {count+1}º produto: R$'))
        vetPrecos.append(preco)

    count += 1

    condicao = ''
    while condicao != 'S' and condicao != 'N':
        condicao = input('deseja continuar?[S/N]: ')
        condicao = condicao.upper()

    if condicao == 'N':
        break

    
valorTotal = 0

for i in range (0, len(vetPrecos)):
        valorTotal += vetPrecos[i]

countProdM = 0

for i in range(0, len(vetPrecos)):

    if vetPrecos[i] > 1000:
        countProdM += 1

    
produtoMaisBarato = ''
valorProdMaisBarato = 0

for i in range(0, len(vetPrecos)):

    if i == 0:
        valorProdMaisBarato = vetPrecos[i]
        produtoMaisBarato = vetProdutos[i]

    else:
        if vetPrecos[i] < valorProdMaisBarato:
            valorProdMaisBarato = vetPrecos[i]
            produtoMaisBarato = vetProdutos[i]


print(f'valor total da compra foi de: R${valorTotal:.2f}')
print(f'{countProdM} produto(s) custa(m) mais de R$1000.00')
print(f'o produto mais barato foi o(a) {produtoMaisBarato}')
