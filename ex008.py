#Programa que lê um valor em metro e converte em centímetros e milímetros

m = float(input('Digite um valor em metros: '))

c = m*100
mm = m*1000

print('{} centímetros\n{} milímetros'.format(c, mm))