def calculate_km():
    try:
        mi = float(input("Enter Miles to convert to Kilometers: "))
        km = mi / 0.62137
        print(f"{mi:.2f} Miles converts to {km:.2f} Kilometers.")
    except ValueError:
        print("Invalid Input. Try again.")
        calculate_km()#using nested function to create a loop

    #the code below is redundant but interesting to look at...

    #making sure object mi is NOT a float before trying again
    # while not isinstance(mi, float):
    #     try:
    #         mi = float(input("Enter Miles to convert to Kilometers: "))
    #         km = mi / 0.62137
    #         print(f"{mi:.2f} Miles converts to {km:.2f} Kilometers.")
    #     except ValueError:
    #         print("Invalid Input. Try again.")
        

calculate_km()