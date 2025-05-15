#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados, 
#B) A lista de valores, ordenada de forma decrescente, C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
count = 0
condicao = 'S'

while condicao == 'S': 
    
    count+=1
    
    lista.append(int(input(f'digite o {count}º número: ')))
    
    condicao = input('deseja ler mais um número? [S/N]: ').strip().upper()
    while condicao != 'S' and condicao != 'N':
        condicao = input('condição inválida. Digite novamente [S/N]: ').strip().upper()



print('='*30)

print(f'foram digitados {count} números.')

print(f'lista ordenada de forma decrescente: {sorted(lista, reverse=True)}')

if 5 in lista:
    
    print('o número 5 foi digitado')

else:

    print('o número 5 não está na lista')


print('='*30)






