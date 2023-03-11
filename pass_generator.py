import random

#caracter = range (32, 127)
#password = []
password_fuente = []
password_variable = str()
a = str()
#print (caracter)

for n in range(0,16):
    caracter = random.randint(32,126)
    #password.append(caracter)
    caracter_fuente = chr(caracter)
    password_fuente.append(caracter_fuente)

for n in range (0,16):
    password_variable += password_fuente[n]
    
    
#print(password)
print(password_fuente)
print(f"Your password is:\t{password_variable}")
