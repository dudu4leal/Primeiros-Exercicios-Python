#Programa que calcula a temperatura em °C e converte pra °F

celcius = float(input('Temperatura em °C: '))

fahrenheit = (celcius*1.8)+32

print('{}°C em fahrenheit é/são: {:.2f}°F'.format(celcius, fahrenheit))