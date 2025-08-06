#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa

from time import sleep

numero1 = float(input('digite o primeiro valor: '))
numero2 = float(input('digite o segundo valor: '))

verificador = False

while verificador == False:

    opcao = int(input('digite a opção desejada:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))

    if opcao == 1:
        print('soma = {}'.format(numero1 + numero2))
        sleep(1)
    elif opcao == 2:
        print('produto = {}'.format(numero1 + numero2))
        sleep(1)
    elif opcao == 3:
        if numero1 > numero2:
            print('{} é maior que {}'.format(numero1, numero2))
            sleep(1)
        elif numero2 > numero1:
            print('{} é maior que {}'.format(numero2, numero1))
            sleep(1)
        else:
            print('os números são iguais')
            sleep(1)

    elif opcao == 4:
        print('digite novos números: ')
        sleep(1)
        numero1 = float(input('digite um novo primeiro valor: '))
        numero2 = float(input('digite um novo segundo valor: '))
        sleep(1)
        
    elif opcao == 5:
        print('fechando aplicação.')
        sleep(1)
        verificador = True


    else:
        print('opção inválida. Tente novamente.')

