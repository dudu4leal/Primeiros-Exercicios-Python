#programa que calcula o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

preço = float(input('valor do produto R$'))

print('formas de pagamento:\n'
    '[1] à vista dinheiro/cheque\n'
    '[2] à vista no cartão\n'
    '[3] em até 2x no cartão\n'
    '[4] 3x ou mais no cartão\n')

formaDePagamento = int(input('forma de pagamento selecionada: '))


if formaDePagamento == 1:
    desconto = preço*0.10
    precoFinal = preço - desconto

    print('valor a ser pago: R${:.2f}'.format(precoFinal))

elif formaDePagamento == 2:
    desconto = preço*0.05
    precoFinal = preço - desconto

    print('valor a ser pago R${:.2f}'.format(precoFinal))

elif formaDePagamento == 3:
    print('o valor será dividido em duas parcelas de R${:.2f} sem juros'.format(preço/2))
    print('valor a ser pago R${:.2f}'.format(preço))

elif formaDePagamento == 4:
    juros = preço*0.20
    precoFinal = preço + juros

    parcelas = int(input('em quantas parcelas quer dividir? '))

    print('seu produto será divido em {} parcelas de R${:.2f} com 20% de juros'.format(parcelas, (precoFinal/parcelas)))
    print('valor a ser pago: R${:.2f}'.format(precoFinal))

else:
    
    print('forma de pagamento inválida.')