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

