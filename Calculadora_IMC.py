"""
Si es debajo de 18.5 UNDERWEIGHT
SI es arriba 18.5 pero debajo de 25 es normal weight
Sí es arriba de 30 pero debajo de 35 es obese
Above 35 es clinically obese
"""

while True:
    estatura = float(input("Ingrese su estatura (m):\t")) 
    peso = float(input("Ingrese su peso corporal (kg):\t"))
    BMI = peso / (pow(estatura,2))
    print (round(BMI,2))
    if BMI <= 18.5:
        print ("You're Underweight")
    elif BMI > 18.5 and BMI <= 25:
        print ("You're Weigth")
    elif BMI > 25 and BMI <= 30:
        print ("You're Overweight") 
    elif BMI > 30 and BMI <= 35:
        print ("You're Obese")
    elif BMI > 35:
        print ("You're Clinically Obese")