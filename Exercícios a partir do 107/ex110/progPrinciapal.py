import moeda

preço = float(input('Digite o preço do produto: R$'))
taxaAumento = int(input('Qual a taxa de aumento?\n'))
taxaRedução = int(input('Qual a taxa de redução?\n'))

moeda.resumo(preço, taxaAumento, taxaRedução)
