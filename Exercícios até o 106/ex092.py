#programa que lê nome, ano de nascimento e carteira de trabalho e cadastra-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcula e acrescenta, além da idade, 
#com quantos anos a pessoa vai se aposentar.

import datetime

nome = str(input('Digite o nome: '))
anoDeNascimento = int(input('Digite o ano de nascimento: '))
carteiraDeTrabalho = int(input('Digite o número da carteira de trabalho (0 se não possuir): '))

hoje = datetime.date.today()
anoAtual = hoje.year

idade = anoAtual - anoDeNascimento

if carteiraDeTrabalho != 0:

    anoDeContratação = int(input('Quando o funcionário foi contratado? '))
    salario = float(input('Informe seu salário: R$ '))

    idadeAposentadoria = (anoDeContratação + 35) - anoDeNascimento

    trabalhador = {'Nome': nome, 'Idade': idade, 'CTPS': carteiraDeTrabalho,
                   'Ano de contratação': anoDeContratação, 'Salário': salario, 'Idade de aposentadoria': idadeAposentadoria} 
    
    for k, v in trabalhador.items():
        print(f'{k} é {v}')

else:

    trabalhador = {'Nome': nome, 'idade': idade, 'ctps': carteiraDeTrabalho}
    
    for k, v in trabalhador.items():
        print(f'{k} é {v}')
