#programa que mostra a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa é interrompido quando o número solicitado é negativo.

n = 0

while True:

    n = int(input('qual tabuada deseja ver? '))
    print('-' * 30)
    
    if n < 0:
        break

    for i in range(1, 11):
        
        valorAtual = n*i

        print(f'{n} x {i} = {valorAtual}')
    print('-' * 30)

print('programa encerrado!')