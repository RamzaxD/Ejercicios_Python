"""Aqui colocaremos nuestro porgrama"""
from persona_class import Persona #importamos nuestra clase persona


def main():
    persons_nums = int(input("Ingrese el número de personas:\t")) #Numero de personas que capuraremos
    persons = [] #Lista para generar los objetos
    #generar una lista de personas:

    def List_View():
        for person_view in range(persons_nums):
            print(f"------PERSONA------")
            persons[person_view].Mostrar_Datos()

    for person_add in range(persons_nums):
        persons.append(person_add) #Generamos una variable
        persons[person_add] = Persona()#la hacemos objeto
        persons[person_add].Date_add()
        #persons[person_add].nombre = input(f"Ingresa el nombre de la Persona:\t") #
        #persons[person_add].edad = int(input(f"Ingrese la edad de la persona:\t"))

    List_View()

    for person_edit in range(persons_nums):
        persons[person_edit].Date_edit()

    List_View()


if __name__ == "__main__":
    main()

"""
persona1 = Persona()#Igualamos la variable con la clase para generar un objeto
persona1.nombre = 'Brayan' #print(f"Ingresa tu nombre:\t")
persona1.edad = 26 #int(print (f"Ingresa tu edad:'t"))
persona1.Mostrar_Datos() #Metodo para mostrar los datos

persona2 = Persona()
persona2 = 'Joel'
persona2 = 30
persona2.Mostrar_Datos()

"""