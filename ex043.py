#programa que lê peso(kg) e altura(m) de uma pessoa, calcula seu IMC e diz a situação do seu índice de massa corporal

import os

peso = float(input('peso em Kg: '))
altura = float (input('altura em metros: '))

imc = peso / altura**2
#print(imc)

if imc < 18.5:
    print('imc = {:.1f}\nabaixo do peso'.format(imc))

elif imc >= 18.5 and imc <= 25:
    print('imc = {:.1f}\npeso ideal'.format(imc))

elif imc > 25 and imc <= 30:
    print('imc = {:.1f}\nsobrepeso'.format(imc))

elif imc > 30 and imc <= 40:
    print('imc = {:.1f}\nobesidade'.format(imc))

elif imc > 40:
    print('imc = {:.1f}\nobesidade mórbida'.format(imc))

os.system("pause")
