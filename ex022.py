#Programa que lê o nome inteiro de uma pessoa e mostra:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Todas as letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:\n')

print(nome.upper())
print(nome.lower())

nomeTam = len(nome.replace(' ', ''))

print(nomeTam)

nomeDividido = nome.split()

primeirNome = nomeDividido[0]

print(len(primeirNome))