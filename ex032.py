#Programa que lê um ano qualquer e mostra se ele é bissexto

import datetime


hoje = datetime.date.today()

esseAno = hoje.year

ano = int(input('Que ano quer analisar? (digite zero para avaliar o ano atual)\n'))


if ano == 0:
    ano = esseAno


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))