#programa que tem uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostra uma listagem de preços, organizando os dados em forma tabular.

tupla_Produdos = (('Arroz', 8.19), ('Feijão', 6.99), ('Batata', 7.50) , ('Leite em Pó', 29.87))

print('-'*39)
print(f'{'LISTAGEM DE PREÇO':^39}')
print('-'*39)




for nome, preços in tupla_Produdos:
    print(f'{nome:.<30} R${preços:> 6.2f}')