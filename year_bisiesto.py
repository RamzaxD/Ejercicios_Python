while True:
    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print(f"year {year} is leap")
        elif year % 100 == 0:
            print(f"year {year} isn't leap")
        else: 
            print(f"year {year} is leap")
    else: print(f"year isn't leap")       

    
    