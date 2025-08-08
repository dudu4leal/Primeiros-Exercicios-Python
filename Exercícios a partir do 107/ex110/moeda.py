def aumentar(preço = 0, taxa = 0, format = True):

    if format == True:

        resp = preço + preço*(taxa/100) 
        
        return moeda(resp)

    elif format == False:

        return preço + preço*(taxa/100) 


def diminuir(preço = 0, taxa = 0, format = True):

    if format == True:

        resp = preço - preço*(taxa/100)

        return moeda(resp)

    elif format == False:

        return preço - preço*(taxa/100) 


def dobro(preço = 0, format = True):

    if format == True:

        resp = preço*2

        return moeda(resp)

    else:

        return preço*2


def metade(preço = 0, format = True):

    if format == True:
        
        resp = preço/2

        return moeda(resp)
    
    else:

        return preço/2


def moeda(preço = 0, moeda = 'R$'):

    return f'{moeda}{preço:.2f}'.replace('.' , ',')


def resumo(valor, taxaAumento, taxaRedução):

    print('-'*31)
    print('RESUMO DO VALOR')
    print('-'*31)

    print('-'*31)

    print(f'{'Valor analisado:':<20} {moeda(valor):>10}')
    print(f'{'Dobro do preço:':<20} {dobro(valor):>10}')
    print(f'{'Metade do preço:':<20} {metade(valor):>10}')
    print(f'{f'{taxaAumento}% de aumento:':<20} {aumentar(valor, taxaAumento):>10}')
    print(f'{f'{taxaRedução}% de redução:':<20} {diminuir(valor, taxaRedução):>10}')

    print('-'*31)
