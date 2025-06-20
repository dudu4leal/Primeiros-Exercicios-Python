# programa que tem uma função chamada contador(), que recebe três parâmetros: início, fim e passo. O programa realiza três contagens através da função criada:
#a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):

    print('='*30)
    print('Contagem de 1 até 10 de 1 em 1:')
    for i in range (1, 11):

        print(f'{i}', end=' ', flush=True)
        sleep(0.5)

    print(' ')


    print('='*30)
    print('Contagem de 10 até 0 de 2 em 2:')
    for i in range(10, -1, -2):
        
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)

    print(' ')


    if passo == 0:
        passo = 1
    
    elif passo < 0:
        passo *= -1


    if fim < inicio:
        if passo > 0:
            passo *= -1
    
        
    print('='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    
    if fim > 0:
    
        for i in range(inicio, fim+1, passo):

            print(f'{i}', end=' ', flush=True)
            sleep(0.5)

    elif fim <= 0:

        for i in range(inicio, fim-1, passo):

            print(f'{i}', end=' ', flush=True)
            sleep(0.5)


#programa principal
a = int(input('Digite o início: '))
b = int(input('Digite o fim: '))
c = int(input('Digite o passo: '))

contador(a, b, c)
