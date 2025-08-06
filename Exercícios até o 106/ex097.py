#programa que tem uma função chamada escreva(), que recebe um texto qualquer como parâmetro e mostra uma mensagem com tamanho adaptável.

def escreva(texto):

    print('='*(len(texto) + 4))
    print(f'  {texto}')
    print('='*(len(texto) + 4))

#Programa principal
imprimir = str(input('Digite o texto que será impresso: '))

escreva(imprimir)
