#Programa que tem uma função chamada voto() que recebe como parâmetro o ano de nascimento de uma pessoa, retorna um valor literal indicando se uma pessoa tem voto
#NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anoNascimento):

    import datetime
    
    hoje = datetime.date.today()
    anoAtual = hoje.year

    idade = anoAtual - anoNascimento

    if idade < 16:
        return 'NÃO VOTA'
    
    elif idade >= 16 and idade < 18:
        return 'OPCIONAL'
    
    elif idade >= 18 and idade <= 70:
        return 'OBRIGATÓRIO'
    
    elif idade > 70:
        return 'OPCIONAL'


n = int(input('Digite o ano de nascimento: '))
print(voto(n))
