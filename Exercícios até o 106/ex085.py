#programa onde o usuário pode digitar sete valores numéricos e cadastra-os em uma lista única que mantém separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

listaGeral = [[], []]

for i in range(0, 7):

    numero = int(input(f'digite o {i+1}º número: '))

    if numero % 2 == 0:

        listaGeral[0].append(numero)
        
    else:

        listaGeral[1].append(numero)


for i in range(0, len(listaGeral)):
    
    listaGeral[i].sort()

print('='*30)

print(f'Os valores pares digitados foram: {listaGeral[0]}')
print(f'Os valores impares digitados foram: {listaGeral[1]}')

print('='*30)