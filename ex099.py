#programa que tem uma função chamada maior(), que recebe vários parâmetros com valores inteiros. O programa analisa todos os valores e diz qual deles é o maior.

def maior(*num):

    print('='*30)

    print(f'Números informados:', end=' ')
    for i in range (0, len(num)):
        print(num[i], end=' ')

    print(f'\nForam informados {len(num)} números ao todo')
    
    
    maiorNumero = 0

    for i in range (0, len(num)):

        if i == 0:
            maiorNumero = num[i]

        else:

            if num[i] > maiorNumero:
                maiorNumero = num[i]
            

    print(f'O maior número é {maiorNumero}')

    print('='*30)
    

#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()