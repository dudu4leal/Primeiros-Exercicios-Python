#programa onde o usuário pode digitar cinco valores numéricos e cadastra-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
#No final, mostra a lista ordenada na tela.

lista = []

for i in range(0, 5):
    
    n = int(input('Digite um valor: '))
    
    if i == 0 or n > lista[-1]:
        
        lista.append(n)
    
    else:
        
        pos = 0
        
        while pos < len(lista):
            
            if n < lista[pos]:
                lista.insert(pos, n)
                break
            
            pos+=1

print('-='*30)
print(f'os valores digitados em ordem foram: {lista}')
                





