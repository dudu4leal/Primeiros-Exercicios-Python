#Programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunta o valor da casa, o salário do comprador 
#e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorDaCasa = float(input('qual o valor da casa?\nR$'))
salario = float(input('qual o salário do comprador?\nR$'))
parcelasAnos = int(input('em quantos anos será parcelada?\n'))

parcelasMeses = parcelasAnos*12
#print(parcelasMeses)
valorPrestacao = valorDaCasa / parcelasMeses
#print(valorPrestacao)

print('cada prestação custará R${:.2f}'.format(valorPrestacao))

if valorPrestacao > salario*0.30:
    print('infelizmente seu empréstimo foi negado.')

else:
    print('seu empréstimo foi aprovado!')