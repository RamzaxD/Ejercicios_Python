# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == ("S" or "s"):
    if add_pepperoni == ("Y" or "y"):
        if extra_cheese == "Y" or "y":
            print (f"Your final bill is: $18.")
        else:
            print(f"Your final bill is: $17.")
    elif add_pepperoni == ("N" or "n"):
        if extra_cheese == ("Y" or "y"):
            print(f"Your final bill is: $16.")
        else:
            print(f"Your final bill is: $15.")
elif size == ("M" or "m"):
    if add_pepperoni == ("Y" or "y"):
        if extra_cheese == ("Y" or "y"):
            print (f"Your final bill is: $24.")
        else:
            print(f"Your final bill is: $23.")
    elif add_pepperoni == ("N" or "n"):
        if extra_cheese == ("Y" or "y"):
            print(f"Your final bill is: $21.")
        else:
            print(f"Your final bill is: $20.")
elif size == ("L" or "l"):
    if add_pepperoni == ("Y" or "y"):
        if extra_cheese == ("Y" or "y"):
            print (f"Your final bill is: $29.")
        else:
            print(f"Your final bill is: $28.")
    elif add_pepperoni == ("N" or "n"):
        if extra_cheese == ("Y" or "y"):
            print(f"Your final bill is: $26.")
        else:
            print(f"Your final bill is: $25.")