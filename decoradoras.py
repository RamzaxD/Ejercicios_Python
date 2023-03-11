def decorarador (func): #función que se le manda otra función

    def decorar(*args): #colcoar siempre arumento indefinido
        print(f"Ejecutando la función {func.__name__}") #plantilla que toma el nombre de la función a decorar
        func(*args) #colocamos la función indefinidamente
        print(f"Terminando de ejecutar la función {func.__name__}")
    return decorar #retornar la función 

@decorarador #colocamos el decorador arriba de la función a decorar
def sumar(a, b):
    total = a+b
    print(f"El total de la suma es de: {total}")

sumar (11,12)

@decorarador
def saludo (nombre):
    print (f"Hola {nombre}")

saludo("Joel")