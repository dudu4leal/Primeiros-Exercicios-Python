#programa que tem a função leiaInt(), que funciona de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):

    ok = False
    valor = 0

    while True:
        
        numero = str(input(msg))

        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')

        if ok:
            break

    return valor


n = leiaInt('Digite um número: ')

print(f'Você digitou o número {n}')

