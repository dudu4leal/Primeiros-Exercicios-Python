#programa que lê um número inteiro e diz se ele é ou não um número primo.

n = int(input('digite o numero: '))
count =0

for i in range (1, n+1):

    if n%i == 0:
        count +=1

if count == 2:
    print('o número {} foi dividido {} vez(es).'.format(n, count))
    print('o número {} é primo'.format(n))
else:
    print('o número {} foi dividido {} vez(es).'.format(n, count))
    print('o número {} não é primo'.format(n))