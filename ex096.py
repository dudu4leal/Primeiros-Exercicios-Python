#programa que tem uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e comprimento) e mostra a área do terreno.

def area(largura, comprimento):

    print(f'A área do terreno com as dimensões {largura}m de largura e {comprimento}m de comprimeto é {largura*comprimento:.2f}m²')


#Programa principal
print('='*30)
print('CONTROLE DE TERRENOS')
print('='*30)

a = float(input('Digite o valor da larguma (em metros): '))
b = float(input('Digite o valor do comprimento (em metros): '))

area(a, b)
