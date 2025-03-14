#Programa que lê o nome de uma cidade e diz se ela começa ou não com a palavra "Santo"

cidade = input('Digite o nome da cidade: ').strip()

if cidade[:5].lower() == 'santo':
    print('Começa com Santo')
else:
    print('Não começa com Santo')