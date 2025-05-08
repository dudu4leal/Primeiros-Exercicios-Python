#programa que tem uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#O programa lê um número pelo teclado (entre 0 e 20) e mostra-o por extenso.

condicao = 'S'

while True:

    numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                       'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
                       'dezenove', 'vinte')

    numero = int(input('digite um número entre 0 20: '))

    while numero < 0 or numero > 20:
        numero = int(input('Valor inválido. Digite um número entre 0 e 20: '))

    print(f'Número digitado por extenso: {numerosPorExtenso[numero]}')

    condicao = input('deseja continuar? [S/N]: ').strip().upper()
    if condicao == 'N':
        break


