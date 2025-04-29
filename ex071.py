#programa que simula o funcionamento de um caixa eletrônico. No início, pergunta ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
#quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valorDoSaque = 0
while True:
    
    valorDoSaque = float(input('Digite o valor que deseja sacar: R$'))

    if isinstance(valorDoSaque, float) and valorDoSaque.is_integer() :
        break
    else:
        print('Inválido. Digite um valor inteiro.')


valorDoSaque = int(valorDoSaque)

notas = [50, 20, 10, 1]

for i in notas:
    
    qtdNotas = int(valorDoSaque / i)
    if qtdNotas != 0:
        print(f'{int(qtdNotas)} nota(s) de RS{i:.2f}')

    valorDoSaque %= i
