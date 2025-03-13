#Programa que indica os tipos primitivos de um valor

n = input('digite algo: ')

print('Qual o tipo primitivo desse valor? {}'.format(type(n)))

print('O valor n só tem espaços? {}'.format(n.isspace()))
print('O valor {} é um número? {}'.format(n, n.isnumeric()))
print('O valor {} é letra? {}'.format(n, n.isalpha()))
print('O valor {} é alphanumérico? {}'.format(n, n.isalnum()))
print('O valor {} está em maiúsculas? {}'.format(n, n.isupper()))
print('O valor {} está em minúsculas? {}'.format(n, n.islower()))