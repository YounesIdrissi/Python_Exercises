name = str(input("Please enter your name: "))
print(f"Welcome {name} to the Distance Converter Application.")

def choices():
    print("Please Enter 1 for Miles to Kilometers conversion.")
    print("Enter 2 for Kilometers to Miles conversion.")
    print("Or Enter 3 to exit the program.")

def calculate_km():
    mi = input("Enter Miles to convert to Kilometers: ")
    km = mi * 1.609
    print(f"{mi} Miles converts to {km} Kilometers.")

def calculate_mi():
    km = input("Enter Kilometers to convert to Miles: ")
    mi = km / 1.609
    print(f"{km} Kilometers converts to {mi} Miles.")

def main_loop():
    choices()
    entry = int(input(""))
    while entry != 3:
        if entry == 3:
            calculate_km()
        elif entry == 2:
            calculate_mi()
        else:
            print("That is not an option.")
        choices()
        entry = int(input(""))
    print("Thank you for using the Distance Converter Application.")

main_loop()
