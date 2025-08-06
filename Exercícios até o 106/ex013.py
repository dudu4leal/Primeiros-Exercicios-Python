#Programa que lê o salário de um funcionário e mostra seu novo salário com 15% de aumento

salario = float(input('Salário atual do funcionário: R$'))

qtdAumento = salario*0.15

salAumentado = salario + qtdAumento

print('Novo salário: R${:.2f}'.format(salAumentado))