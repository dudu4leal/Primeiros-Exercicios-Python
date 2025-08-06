#Programa que lê o nome completo de uma pessoa e mostra seu primeiro e seu último nome

nome = input('Digite seu nome: ')
nome = nome.title()

nomeDividido = nome.split()
print('Primeiro nome: {}'.format(nomeDividido[0]))

nomeInvertido = nomeDividido[::-1]
print('Último nome: {}'.format(nomeInvertido[0]))
