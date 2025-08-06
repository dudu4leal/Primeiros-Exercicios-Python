#Programa que lê a altura e a largura de uma parede e calcula sua área e quanto de tinta vai ser necessário para pinta-la 
#Cada litro pinta 2 metros quadrados

altura = float(input('altura da parede: '))
largura = float(input('largura da parede: '))

area = largura*altura

qtdTinta = area/2

print('Área = {:.2f} m²\nQuantidade de tinta necessária: {:.2f} l'.format(area, qtdTinta))