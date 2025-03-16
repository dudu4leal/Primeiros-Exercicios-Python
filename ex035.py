#Programa que lê o comprimento de três retas e diz ao usuário se elas podem ou não formar um triângulo

a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))

#if c < (a+b):
#    if b < (a+c):
#       if a < (b+c):
#           print('esse triângulo pode existir!')
#        else:
#            print('esse triângulo não pode existir.')
#    else:
#        print('esse triângulo não pode existir.')
#else:
#    print('esse triângulo não pode existir.')

#ignorem a lambamça que fiz antes haha, não pensei direiro


if c < (a+b) and b < (a+c) and c < (a+b):
    print('esse triângulo pode existir!')
else:
    print('esse triângulo não pode existir')