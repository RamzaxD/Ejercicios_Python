# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() #el split hace una lista solo str por cada dato que pongas más un espacio (123 123 123)
for n in range(0, len(student_heights)):#transforma los valores en int
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

suma = 0
#Write your code below this row 👇

for n in range(0, len(student_heights)):
    suma += student_heights[n]   
#print (suma)

promedio = suma/ len(student_heights)
#print(f"{promedio}")
promedio = round(promedio, 0)
print (f"El promedio de estaturas es:\t{int(promedio)}")
