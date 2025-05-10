#programa que lê quatro valores pelo teclado e guarda-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))
#n3 = int(input('Digite o terceiro valor: '))
#n4 = int(input('Digite o quarto valor: '))

tupla = (
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º número: ')),
    int(input('Digite o 4º número: '))
)

count_Nove = 0
posicao_Tres = -1
valores_Pares = []

for i in range (0, len(tupla)):

    if tupla[i] == 9:
        count_Nove +=1

for i in range(0, len(tupla)):

    if tupla[i] == 3:
        posicao_Tres = i
        break

for i in range (0, (len(tupla))):

    if tupla[i] % 2 == 0:
        valores_Pares.append(tupla[i])

print(f'O número 9 aparece {count_Nove} vezes')


if posicao_Tres == -1:
    print('o número 3 não está na tupla')
else:
    print(f'o numero 3 aparece pela primeria vez na posição {posicao_Tres}')


print(f'O(s) número(s) pares da tupla foi(foram): {valores_Pares}')
