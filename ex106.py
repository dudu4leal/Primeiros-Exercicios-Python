#mini-sistema que utiliza o Interactive Help do Python. O usuário digita o comando e o manual aparece. Quando o usuário digitaa a palavra ‘FIM’, o programa se encerrará. 

from time import sleep


while True:

    print('^'*23)
    print('Sistema de ajuda PyHELP')
    print('^'*23)
    sleep(0.5)

    função_ou_biblioteca = str(input('Função ou biblioteca > ')).strip().lower()
    sleep(0.5)
    

    if função_ou_biblioteca == 'fim':

        print('^'*8)
        print('Até logo!')
        print('^'*8)

        break


    print('^'*35)
    print(f'Acessando o manual do comando {função_ou_biblioteca}')
    print('^'*35)
    sleep(0.5)

    help(função_ou_biblioteca)
