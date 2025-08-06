#programa que lê números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostra quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)

n = count = soma = 0

while True:
   
    n = int(input('digite um número (999 para parar): '))

    if n == 999:
        break

    count += 1
    soma += n

print(f'foram digitados {count} e a soma deles foi {soma}')