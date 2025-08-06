#programa onde o usuário digita uma expressão qualquer que usa parênteses. O aplicativo analisa se a expressão passada está com os parênteses abertos e fechados
# na ordem correta.

expressao = input('digite sua expressão algébrica com parenteses: ')
pilha = []


for elemento in expressao:
    
    if elemento == '(':
        pilha.append('(')

    elif elemento == ')':

        if len(pilha) > 0:
            pilha.pop()

        else:
            pilha.append(')')
            break

if len(pilha) == 0:

    print('Sua expressão está correta!')

else:

    print('Sua expressão está errada.')
    