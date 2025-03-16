#Programa que lê três números e mostra qual é o maior e qual é o maior.

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo número: '))
n3 = float (input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('o primeiro número ({}) é o maior'.format(n1))
    else:
        print('o terceiro número ({})é o maior'.format(n3))
else:
    if n2 > n3:
        print('o segundo número ({}) é o maior'.format(n2))
    else:
        print('o terceiro número {} é o maior'.format(n3))