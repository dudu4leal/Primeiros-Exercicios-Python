#Programa em que lê um número inteiro qualquer e pede para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('digite um número inteiro: '))

print('digite 1 para converter em binário\ndigite 2 para converter em octal\ndigite 3 para hexadecimal')

base = int(input('escolha a base para converter: '))


if base == 1:
    conversao = bin(numero)[2:]
    print('o número {} convertido para a base binária é {}'.format(numero, conversao))

elif base == 2:
    conversao = oct(numero)[2:]
    print('o número {} convertido para a base octal é {}'.format(numero, conversao))

elif base == 3:
    conversao = hex(numero)[2:]
    print('o número {} convertido para a base hexadecimal é {}'.format(numero, conversao))

else:
    print('escolha inválida')