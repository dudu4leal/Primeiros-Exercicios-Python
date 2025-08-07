import moeda

preço = float(input('Digite o preço do produto: R$'))
taxaAumento = int(input('Qual a taxa de aumento?\n'))
taxaRedução = int(input('Qual a taxa de redução?\n'))

print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
print(f'Aumentando {taxaAumento}%, temos {moeda.aumentar(preço, taxaAumento)}')
print(f'Reduzindo {taxaRedução}%, temos {moeda.diminuir(preço, taxaRedução)}')
