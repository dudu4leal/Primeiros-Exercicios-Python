#refazendo exercício 51 utilizando "while"

primeiroTermo = int(input('qual o primeiro termo da P.A. ?\n'))
razao = int(input('qual a razão da P.A.  ?\n'))
termoAtual = primeiroTermo
count = 0

print('P.A. = ', end=' ')
while count < 10:
    print('{} -->'.format(termoAtual), end=' ')

    termoAtual += razao
    count += 1

    

print('fim.')