#Programa que sorteia o nome de um aluno para apagar o quadro

import random

aluno1 = input('digite o primeiro aluno: ')
aluno2 = input('digite o segundo aluno: ')
aluno3 = input('digite o terceiro aluno: ')
aluno4 = input('digite o quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(lista)

print('o aluno sorteado foi: {}'.format(sorteio))