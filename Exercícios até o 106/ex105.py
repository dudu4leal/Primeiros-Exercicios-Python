#programa que tem uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*notas, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.

    Args:
        
    - notas: Notas dos alunos. Pode ser quantas quiser
    - sit: valor opcional, indica se deve ou não colocar a situação
    
    Returns:
    
    Dicionário com várias informações sobre a situação da turma
    """

    maior = 0
    menor = 0
    soma = 0
    count = 0
    situação = ''

    for i, nota in enumerate(notas):

        if i == 0:
            maior = nota
            menor = nota

        else:

            if nota > maior:
                maior = nota

            elif nota < menor:
                menor = nota

        soma += nota
        count += 1

    media = round(soma/count, 1)

    if media < 6:
        situação = 'RUIM'

    elif media > 6 and media < 7:
        situação = 'OK'

    else: 
        situação = 'BOA'


    if sit == False:
        
        dict = {'Total de notas': count,
                'Maior nota': maior, 
                'Menor nota': menor,
                'Média da turma': media}

    elif sit == True:

        dict = {'Total de notas': count,
                'Maior nota': maior, 
                'Menor nota': menor,
                'Média da turma': media,
                'Situação': situação}
        
    return dict


resp = notas(5.5, 2.5, 10)
print(resp)
help(notas)
