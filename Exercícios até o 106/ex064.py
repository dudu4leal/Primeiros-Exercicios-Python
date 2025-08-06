#programa que lê vários números inteiros pelo teclado. O programa só para quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int(input('digite o número: '))
count = 0
soma = 0

while numero != 999:
    
    count += 1
    soma += numero

    numero = int(input('digite mais um número (999 se quiser parar): '))


print('foram lidos {} números.\nA soma deles foi {}'.format(count, soma))
