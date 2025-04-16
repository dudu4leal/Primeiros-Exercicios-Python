#programa que lê o sexo de uma pessoa, mas só aceita os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

verificador = False

while verificador == False:
    sexo = input('digite o seu sexo (M/F): ')
    sexo = sexo.upper()

    if sexo == 'M' or sexo == 'F':

        if sexo == 'M':
            print('você é um homem.')
        else:
            print('você é mulher.')
        
        verificador = True
    else:
        print('sexo inválido. Digite novamente.')
