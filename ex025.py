#Programa que lê o nome de uma pessoa e diz se ela tem "Silva" no nome

nome = input('Digite o seu nome: ')

nome = nome.upper()

if 'SILVA' in nome:
    print('Esta pessoa tem Silva no nome\n')
else:
    print('Esta pessoa não tem Silva no nome')