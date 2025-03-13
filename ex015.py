#Programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorridos = float(input('Quantos Km o carro percorreu?\n'))
diasAlugados = float(input('Quantos dias o carro ficou alugado?\n'))

totalAluguel = 60*diasAlugados + 0.15*kmPercorridos

print('O total do aluguel foi R${:.2f}'.format(totalAluguel))
