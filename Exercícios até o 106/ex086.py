#programa que declara uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
#No final, mostra a matriz na tela, com a formatação correta.

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
