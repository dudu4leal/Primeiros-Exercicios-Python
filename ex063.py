#Programa que lê um número N inteiro qualquer e mostra na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input('digite quantos termos da sequência quer ver: '))

vetor = []
count = 0

while count < n:

    if count == 0:
        vetor.append(0)
    
    elif count == 1:
        vetor.append(1)

    else:
        vetor.append(vetor[count-1] + vetor[count-2])

    count += 1

#print(vetor) 

for i in range(0, n):
    
    print('{} --> '.format(vetor[i]), end='')

print('FIM')