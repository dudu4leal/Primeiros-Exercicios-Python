#Programa que sorteia ordem de 4 alunos para a apresentação de um trabalho 

import random

aluno1 = input('primeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print('ordem dos alunos: {}'.format(lista))