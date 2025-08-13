from lib.interface import *
from time import sleep

opção = 0

while True:

    opção = escolha()

    if opção == 1:

        sleep(0.3)
        print(linha())
        visualizarPessoas()
        sleep(0.3)


    elif opção == 2:

        print(linha())
        print('NOVO CADASTRO'.center(42))

        sleep(0.3)
        print(linha())
        nome = str(input('Nome: ')).strip().title()
        
        idade = leiaInt('Idade: ')
        idade = str(idade)

        cadastrarPessoas(nome, idade)
        
        sleep(0.3)
        print(linha())
        print(f'Novo registro de {nome} adicionado')
        sleep(1)


    elif opção == 3:

        sleep(0.3)
        print(linha())
        print('Saindo do sitema... Até logo!')
        print(linha())
        sleep(0.3)
        
        break
