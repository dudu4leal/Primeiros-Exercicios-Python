#programa que lê 5 valores numéricos e guarda-os em uma lista. No final, mostra qual foi o maior e o menor valor digitados e as suas respectivas posições na lista.

numeros = []
count = 0

while count < 5:
    numeros.append(int(input(f'Digite o {count+1}º valor da lista: ')))
    count+=1

#print(numeros)

maiorValor = -1
menorValor = -1

for i in range(0, len(numeros)):

    if i == 0:

        maiorValor = numeros[i]
        menorValor = numeros[i]

    else:
        
        if numeros[i] > maiorValor:
            maiorValor = numeros[i]
        
        elif numeros[i] < menorValor:
            menorValor = numeros[i] 

posMaiores = []
posMenores = []

for i in range (0, len(numeros)):
    
    if numeros[i] == maiorValor:
        posMaiores.append(i)

    elif numeros[i] == menorValor:
        posMenores.append(i)

maiores = ', '.join(map(str, posMaiores))
menores = ', '.join(map(str, posMenores))


print(f'O maior valor foi {maiorValor} encontrado nas posições {maiores}')
print(f'O menor valor foi {menorValor} encontrado nas posições {menores}')
