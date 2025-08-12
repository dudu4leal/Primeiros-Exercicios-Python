def leiaDinheiro(texto):


    while True:

        valor = input(texto).strip()
        valor = valor.replace(',', '.')

        try:
        
            valor = float(valor)
            
            if valor < 0:
                print(f'ERRO! "{valor}" é um preço negativo')
            
            else:
                return valor

        
        except:

            print(f'ERRO! "{valor}" é um preço inválido')

