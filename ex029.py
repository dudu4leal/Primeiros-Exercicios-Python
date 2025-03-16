#Programa que lê a velocidade de um carro. Se ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('qual velocidade registrada?(em km/h)\n'))

if velocidade > 80:
    print('veículo multado.')

    valorMulta = float((velocidade - 80)*7)

    print('valor da multa: R${:.2f}'.format(valorMulta))
else:
    print('veículo não foi multado. Tenha um bom dia e dirija com segurança!')