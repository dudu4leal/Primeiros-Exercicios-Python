#Programa que recebe um número inteiro e mostra sua tabuada

n = int(input('Qual tabuada deseja calcular?\n'))

for i in range(1, 11):
    resultado = n*i
    print('{} X {} = {}'.format(n, i, resultado))
