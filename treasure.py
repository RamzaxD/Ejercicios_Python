# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
#print (map)
print(f"{row1}\n{row2}\n{row3}")#Formatea la listas para que quede en cuadros
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
treasure = "X"
position = int(position)

if (position == 11) or (position == 12) or (position == 13):
    if position == 11:
        map[0][0] = treasure
    elif position == 12:
        map[1][0] = treasure
    elif position == 13:
        map[2][0] = treasure
elif (position == 21) or (position == 22) or (position == 23):
    if position == 21:
        map[0][1] = treasure
    elif position == 22:
        map[1][1] = treasure
    elif position == 23:
        map[2][1] = treasure
elif (position == 31) or (position == 32) or (position == 33):
    if position == 31:
        map[0][2] = treasure
    elif position == 32:
        map[1][2] = treasure
    elif position == 33:
        map[2][2] = treasure

#print (map)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
