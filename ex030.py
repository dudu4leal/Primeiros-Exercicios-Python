#Programa que lê um número inteiro e mostra na tela se ele é PAR ou ÍMPAR

numero = int(input('digite um número: '))

if numero % 2 == 0:
    print('{} é um número par!'.format(numero))
else:
    print('{} é um número ímpar'.format(numero))