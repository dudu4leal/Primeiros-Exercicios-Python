#Aprimorando o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha

matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):

        numero = int(input(f'digite o número da posição linha [{i+1}] e coluna [{j+1}] da matriz: '))
        
        if i == 0:
            matriz[0].append(numero)

        elif i == 1:
            matriz[1].append(numero)

        elif i == 2:
            matriz[2].append(numero)

#print(matriz)

print('='*50)

print('a matriz é: ')
for i in range(0, 3):

    print(matriz[i])

print('='*50)


somaValoresPares = 0
somaValoresTerceira = 0
maiorValorS = 0


for i in range (0, 3):
    for j in range (0, 3):
        
        if matriz[i][j] % 2 == 0:
            somaValoresPares += matriz[i][j]

        if j == 2:
            somaValoresTerceira += matriz[i][j]

        if i == 1:

            if matriz[i][j] > maiorValorS:
                maiorValorS = matriz[i][j]


print(f'Soma dos valores pares da matriz é: {somaValoresPares}')
print('='*50)

print(f'Soma dos valores da 3ª coluna: {somaValoresTerceira}')
print('='*50)

print(f'Maior valor da 2ª linha: {maiorValorS}')
print('='*50)
