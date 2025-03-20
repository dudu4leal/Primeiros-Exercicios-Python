#Programa que lê dois números inteiros e os compara, mostrando na tela quem é maior ou se eles são iguais

numero1 = int(input('primeiro número: '))
numero2 = int(input('segundo número: '))

if numero1 > numero2:
    print('o primeiro número é maior')
elif numero2 > numero1:
    print('o segundo número é maior')
else:
    print('os dois números são iguais')