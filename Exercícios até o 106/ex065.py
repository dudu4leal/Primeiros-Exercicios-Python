#programa que lê vários números inteiros pelo teclado. No final da execução, mostra a média entre todos os valores 
#e qual foi o maior e o menor valores lidos. O programa pergunta ao usuário se ele quer ou não continuar a digitar valores.

condicao = 'S'
soma = 0
maiorValor = 0
menorValor = 0
count = 0

while condicao == 'S':
    
    numero = int(input('digite um número: '))

    soma += numero

    if count == 0:

        maiorValor = numero
        menorValor = numero
    
    else:

        if numero > maiorValor:
            maiorValor = numero
        
        elif numero < menorValor:
            menorValor = numero

    count += 1
    
    condicao = input('Quer ler mais um número? Digite S para sim e N para Não: ')
    condicao = condicao.upper()

    while condicao != 'S' and condicao != 'N':
    
        condicao = input('valor inválido. Digite novamente [S/N]: ')
        condicao = condicao.upper()
    

media = float(soma/count)   

print('a média dos valores lidos foi {:.2f}\nO maior valor foi {} e o menor valor foi {}'.format(media, maiorValor, menorValor))