#Write your code below this line 👇
from math import ceil

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   
def paint_calc(height, width, cover):
    area = height * width
    if area % 5 == 0:
        cover = area // coverage
        print (f"You need {cover} coverages")
    else: 
        cover = ceil (area/coverage)
        print (f"You need {cover} coverages")
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
