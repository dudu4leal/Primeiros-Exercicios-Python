#Programa que lê o preço de um produto e informa seu novo preço com 5% de desconto

preco = float(input('Preço original do produto: R$'))

desconto = preco*0.05

precoComDesconto = preco - desconto

print('Preço original do produto: R${:.2f}'.format(preco))
print('Preço do produto com desconto: R${:.2f}'.format(precoComDesconto))