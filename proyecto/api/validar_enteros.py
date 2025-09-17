def validar_enteros(mensaje):

    while True:
        try:
            return int(input(mensaje))
        
        except ValueError:
            print("ingresa un numero valido: ")