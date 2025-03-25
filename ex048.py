#Programa que calcula a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
qtdValores = 0

for i in range (1, 501):

    if i%3 == 0:
        if i%2 != 0:
            qtdValores +=1
            soma+=i

print(' a soma dos {} valores é: {}'.format(qtdValores, soma))