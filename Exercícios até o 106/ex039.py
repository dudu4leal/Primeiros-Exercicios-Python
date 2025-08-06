#programa que lê o ano de nascimento de um jovem e informa, de acordo com a sua idade, se ele ainda vai se alistar 
#ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#o programa também mostra o tempo que falta ou que passou do prazo.

import datetime

anoDeNascimento = int(input('ano de nascimento: '))

hoje = datetime.date.today()

anoAtual = hoje.year
#print(anoAtual)

idade = anoAtual - anoDeNascimento

if idade < 18:
    print('você ainda terá que se alistar')
    tempoRestante = 18 - idade
    print('ainda falta(m) {} ano(s)'.format(tempoRestante))
elif idade == 18:
    print('está na hora de se alistar!')
else:
    print('já passou da hora de se alistar...')
    tempoExcedente = idade - 18
    print('já se passou/passaram {} ano(s) do prazo'.format(tempoExcedente))