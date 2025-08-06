#programa que tem uma função fatorial() que recebe dois parâmetros: o primeiro que indica o número a calcular e outro chamado show, 
#que é um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número

    Parâmetros:
        n: Número que será calculado
        show: False: não mostra a conta. True: Mostra a conta 
        Defaults to False.

    Returns:
        O valor do fatorial de um número n
    """

    resultado = 1

    if show == False:
        
        for i in range (n, 0, -1):
            resultado *= i
    
        return resultado


    elif show == True:

        for i in range (n, 0, -1):

            print(i, end='')
            if i > 1:
                print(' x ', end='')

            else:
                print(' = ', end='')

            resultado *= i
    
        return resultado
        

print(fatorial(5))
print(help(fatorial))
