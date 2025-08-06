#Programa que pergunta a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0,50 por Km para 
#viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('distancia do destino desejado: '))

if distancia <= 200:
    valorPassagem = distancia*0.50
    print('valor da passagem: R${:.2f}'.format(valorPassagem))
else:
    valorPassagem = distancia*0.45
    print('valor da passagem: R${:.2f}'.format(valorPassagem))