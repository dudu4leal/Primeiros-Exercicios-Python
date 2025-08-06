#Programa que lê o comprimento de três retas e diz ao usuário se elas podem ou não formar um triângulo
#Agora ele diz qual tipo de triângulo será formado, caso ele possa existir

a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))


if a + b > c and a + c > b and b + c > a:
    print('esse triângulo pode existir!')
    
    if a == b and b==c and a ==c:
        print('todos os lados são iguais\nserá formado um triângulo equilátero')

    elif a == b or b == c or a == c:
        print('dois lados são iguais\nserá formado um triângulo isósceles')

    elif a != b and b != c and a != c:
        print('todos os lados são diferentes\nserá formado um triângulo escaleno')


else:
    print('esse triângulo não pode existir')