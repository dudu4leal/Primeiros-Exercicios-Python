#Programa que lê seis números inteiros e mostra a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, ele é desconsiderado.

soma = 0

for i in range(0,6):

    n = int(input('digite o {}° número: '.format(i+1)))
    
    if n%2 == 0:
        soma+=n

print('a soma dos valores pares é: {}'.format(soma))