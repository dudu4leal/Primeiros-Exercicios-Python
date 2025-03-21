#progrma que lê o ano de nascimento de um atleta e mostra sua categoria

import datetime

anoNascimento = int(input('ano de nascimento: '))
hoje = datetime.date.today()
anoAtual = hoje.year

idade = anoAtual - anoNascimento
#print(idade)

if idade <= 9:
    print('idade: {}\natleta mirim'.format(idade))
elif idade >=10 and idade <= 14:
    print('idade: {}\natleta infantil'.format(idade))
elif idade >=15 and idade <= 19:
    print('idade: {}\natleta junior'.format(idade))
elif idade >=20 and idade <= 25:
    print('idade: {}\naltetla sênior'.format(idade))
elif idade > 25:
    print('idade: {}\natleta master'.format(idade))