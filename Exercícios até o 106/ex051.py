#Programa que lê o primeiro termo e a razão de uma PA. No final, mostra os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('qual o primeiro termo da P.A. ?\n'))
razao = int(input('qual a razão da P.A.  ?\n'))
termoAtual = primeiroTermo

print('P.A. = ', end=' ')
for i in range(0, 10):
    print('{} -->'.format(termoAtual), end=' ')

    termoAtual += razao

print('fim.')