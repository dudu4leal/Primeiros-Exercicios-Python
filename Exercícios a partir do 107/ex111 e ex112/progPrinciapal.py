from utilidadescev import moeda, dados


preço = dados.leiaDinheiro('Digite o preço R$')
taxaAumento = int(input('Qual a taxa de aumento?\n'))
taxaRedução = int(input('Qual a taxa de redução?\n'))

moeda.resumo(preço, taxaAumento, taxaRedução)
