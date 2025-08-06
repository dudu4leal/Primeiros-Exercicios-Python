#programa que gera cinco números aleatórios e coloca em uma tupla. Depois disso, 
#mostra a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

tuplaAleatoria = tuple(random.randint(0, 10) for _ in range (0, 5))

print(f'Numeros gerados: {tuplaAleatoria}')

maiorValor = 0
menorValor = 0

#for i in range(0, len(tuplaAleatoria)):
    
#    if i == 0:
#        
#        maiorValor = tuplaAleatoria[i]
#        menorValor = tuplaAleatoria[i]

#    else:

#        if tuplaAleatoria[i] > maiorValor:
        
#            maiorValor = tuplaAleatoria[i]

#        elif tuplaAleatoria[i] < menorValor:

#            menorValor = tuplaAleatoria[i]

print(f'o maior valor é: {max(tuplaAleatoria)}')
print(f'o menor valor é: {min(tuplaAleatoria)}')
