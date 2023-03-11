# 🚨 Don't change the code below 👇
while True:
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    name1 = name1.lower()
    name2 = name2.lower()

    names = name1 + name2

    count1 = (names.count("t") + names.count("r") + names.count("u") + names.count("e"))  
    count2 = (names.count("l") + names.count("o") + names.count("v") + names.count("e")) 
    print(count1)
    print(count2)
    love = str(count1) + str(count2)
    love = int(love)
    if (love <= 10) or (love >= 90):
        print(f"Your score is {love}, you go together like coke and mentos.")
    elif (love >= 40) and (love <= 50):
        print(f"Your score is {love}, you are alright together.")
    else:
        print(f"Your score is {love}.")