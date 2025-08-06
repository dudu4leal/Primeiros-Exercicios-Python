#Melhorando o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('qual o primeiro termo da P.A. ?\n'))
razao = int(input('qual a razão da P.A.  ?\n'))
termoAtual = primeiroTermo
count = 0

print('P.A. = ', end=' ')
while count < 10:
    print('{} -->'.format(termoAtual), end=' ')

    termoAtual += razao
    count += 1
print('PAUSA')

maisAlgum = int(input('\ndeseja mostrar mais quantos termos? Resp: '))

qtdElementos = 0

while maisAlgum != 0: 
    qtdElementos += maisAlgum
    count = 0

    while count < maisAlgum:
        print('{} -->'.format(termoAtual), end=' ')

        termoAtual += razao
        count += 1

    print('PAUSA')

    maisAlgum = int(input('\ndeseja mostrar mais quantos termos? Resp: '))


    
print('progressão finalizada com {} termos mostrados'.format(qtdElementos+10))