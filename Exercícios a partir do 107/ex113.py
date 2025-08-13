#Reescrevendo a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# criando também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):

    while True:

        try:

            valor = int(input(msg))

            return valor

        except (ValueError, TypeError):

            print(f'ERRO! Digite um número inteiro válido.')

        except KeyboardInterrupt:

            print('Entrada de dados interrompida pelo usuário.')
            return 0 
        


def leiaFloat(msg):

    while True:

        try:

            valor = float(input(msg))

            return valor

        except (ValueError, TypeError):

            print(F'ERRO! Digite um número real válido.')

        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            return 0




inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')

print(f'O número inteiro digitado foi: {inteiro}')
print(f'O número real digitado foi: {real}')
