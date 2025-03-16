#Programa que pergunta o salário de um funcionário e calcula o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcula um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('qual o salário: '))

if salario > 1250:
    novoSalario = salario + (salario*0.10)
else: 
    novoSalario = salario + (salario*0.15)

print('novo salário = R${:.2f}'.format(novoSalario))