#Programa que converte Reais em Dólares

reais = float(input("Valor: R$"))

dolares = reais/5.82 #Cotação do Dólar dia 13/03/2025 (segundo o site "Wise")

print('Você comprou ${:.2f}'.format(dolares))
