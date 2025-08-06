#Programa que lê o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lidos.

maiorPeso = 0
menorPeso = 0 
for i in range(0,5):
    peso = float(input('digite o peso em Kg da {}° pessoa: '.format(i+1)))

    if i == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso


print('o maior peso lido foi {:.1f} Kg\n'
    'e o menor peso lido foi {:.1f} Kg'.format(maiorPeso, menorPeso))