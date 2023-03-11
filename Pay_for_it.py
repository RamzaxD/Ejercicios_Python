# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #Separa los elementos de la cadena y los hace lista por cada ", " que vea
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
no = len(names)
print(names)
person = random.randint (0, no)
print (f"{names[person]} is going to buy the meal today!")
