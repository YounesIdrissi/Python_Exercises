#Distance Converter - Functional Program

name = str(input("Please enter your name: "))
print(f"-------- Welcome {name} to the Distance Converter Application --------")


def choices():#reusable lines of code; best to put them in a function
    print("Please Enter 1 for Miles to Kilometers conversion.")
    print("Enter 2 for Kilometers to Miles conversion.")
    print("Or Enter 3 to exit the program.")
    print()#line space for terminal aesthetic; better UX


def calculate_km():
    #error handling to keep out invalid input
    try:
        mi = float(input("Enter Miles to convert to Kilometers: "))
        km = mi / 0.62137
        print(f"{mi:.2f} Miles converts to {km:.2f} Kilometers.")
    except ValueError:
        print("Invalid Input. Try entering numbers only.")
        #using nested function to create a recursive loop
        calculate_km()#reiterate error handling until no more exceptions/errors


def calculate_mi():
    #error handling to keep out invalid input
    try:
        km = float(input("Enter Kilometers to convert to Miles: "))
        mi = km * 0.62137
        print(f"{km:.2f} Kilometers converts to {mi:.2f} Miles.")
    except ValueError:
        print("Invalid Input. Try entering numbers only.")
        #using nested function to create a recursive loop
        calculate_mi()#reiterate error handling until no more exceptions/errors


#main loop function handles all the other functions; this is the executable
def main_loop():
    while True:
        #error handling to keep out invalid input
        try:
            choices()
            entry = int(input(""))
        except ValueError:
            print("Invalid Input. Try entering integers only.")
            entry = 0#assign new value to entry to prevent referencing last valid entry

        print()#line space for terminal aesthetic; better UX
        if entry == 1:
            calculate_km()
        elif entry == 2:
            calculate_mi()
        elif entry == 3:
            break
        else:#handles anything which isn't a valid input
            print("That is not an option.")
            
        print()#line space for terminal aesthetic; better UX

    print("-------- Thank you for using the Distance Converter Application --------")


main_loop()
