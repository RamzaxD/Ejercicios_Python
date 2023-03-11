"""Aqui encontraremos las clases de nuestro programa"""
class Persona: #se inicia con mayusculas el nombre de la clase.
    #ATRIBUTOS
    __nombre = None #Encapsulado de atributos
    __edad = None
    __ansewr = None
    
    def Date_add (self):
        self.__nombre = input(f"Ingresa el nombre de la Persona:\t")
        self.__edad = int(input(f"Ingresa la edad de la Persona:\t"))
    """
    #CONSTRUCTOR
    def __init__(self, nombre, edad):#Se ejecutara al crear un objeto de esta clase
        self.nombre = nombre
        self.edad = edad
    """
    #METODOS
    def Mostrar_Datos(self): #se coloca self para indicar que es parte de las clases.
        print (f'Su nombre es:\t {self.__nombre}') #hay que colocar el self para que identique el atributo de la clase
        print (f'Su edad es:\t {self.__edad}')

    def Date_edit (self):
        self.__ansewr = input(f'¿Desea editar los datos? (y/n):\t')
        if (self.__ansewr == "y") or (self.__ansewr == "Y"):
            Persona.Date_add(self)
            print(f"-----New Person Dates-----:")
            Persona.Mostrar_Datos(self)
            print(f"\n\n\n")
        elif (self.__ansewr == "n") or (self.__ansewr == "N"):
            Persona.Mostrar_Datos(self)




