#programa que lê duas notas de um aluno e calcula sua média e mostrando uma mensagem no final, de acordo com a média atingida

nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print('aluno em recuperação.')

    if nota1 > nota2:
        notaMaior = nota1
    else:
        notaMaior = nota2

    notaRecuperacao = float(input('nota da recuperação: '))

    mediaFinal = (notaMaior + notaRecuperacao) / 2

    if mediaFinal >= 7.0:
        print('aluno aprovado!')
    else:
        print('aluno reprovado')

else:
    print('aluno aprovado!')