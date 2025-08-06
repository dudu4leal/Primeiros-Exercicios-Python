#Programa que lê um número de 0 a 9999 e mostra qual dígito está na casa da unidade, dezena, centra e milhar

numero = int(input('Digite um numero entre 0 e 9999: '))

while numero >=10000 or numero < 0:
    print('Numero inválido.\nDigite novamente: ')
    numero = int(input('Digite um numero entre 0 e 9999: '))


numeroS = str(numero).zfill(4)

print('Unidade: {}'.format(numeroS[3:4]))
print('Dezena: {}'.format(numeroS[2:3]))
print('Centena: {}'.format(numeroS[1:2]))
print('Milhar: {}'.format(numeroS[:1]))