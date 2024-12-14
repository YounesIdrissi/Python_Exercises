#Distance Converter ; Object-Oriented Approach
'''
Classes & their instances allow for better organization of Logic and Data.
Unlike Functional Programming, OOP allows for the avoidance of global variable
declaration, which improves maintainability (less spaghetti code).
'''
#This version also resolves the redundancy of the last else statement in the mainloop

class Converter:
    def __init__(self, entry):
        self.entry = entry


    def intro(self):
        name = str(input("Please enter your name: "))
        print(f"-------- Welcome {name} to the Distance Converter Application --------")


    def choices(self):#reusable lines of code; best to put them in a function
        print("Please Enter 1 for Miles to Kilometers conversion.")
        print("Enter 2 for Kilometers to Miles conversion.")
        print("Or Enter 3 to exit the program.")
        print()#line space for terminal aesthetic; better UX


    def calculate_km(self):
        #error handling to keep out invalid input
        try:
            mi = float(input("Enter Miles to convert to Kilometers: "))
            km = mi / 0.62137
            print(f"{mi:.2f} Miles converts to {km:.2f} Kilometers.")
        except ValueError:
            print("Invalid Input. Try entering numbers only.")
            #using nested function to create a recursive loop
            convert.calculate_km()#reiterate error handling until no more exceptions/errors


    def calculate_mi(self):
        #error handling to keep out invalid input
        try:
            km = float(input("Enter Kilometers to convert to Miles: "))
            mi = km * 0.62137
            print(f"{km:.2f} Kilometers converts to {mi:.2f} Miles.")
        except ValueError:
            print("Invalid Input. Try entering numbers only.")
            #using nested function to create a recursive loop
            convert.calculate_mi()#reiterate error handling until no more exceptions/errors

    
    def error_handling(self):
        #error handling to keep out invalid input
        try:
            convert.choices()
            self.entry = int(input(""))
        except ValueError:
            print("Invalid Input. Try entering integers only.")
            convert.error_handling()


    #main loop function handles all the other functions; this is the executable
    def main_loop(self):
        convert.intro()
        while True:
            #error handling initialization; getting initial user input
            try:
                convert.choices()
                self.entry = int(input(""))
            except ValueError:
                print("Invalid Input. Try entering integers only.")
                #using nested function to create a recursive loop
                convert.error_handling()#reiterate until no more errors/exceptions

            print()#line space for terminal aesthetic; better UX
            if self.entry == 1:
                convert.calculate_km()
            elif self.entry == 2:
                convert.calculate_mi()
            elif self.entry == 3:
                break
            else:#handles invalid integer options
                print("That is not an option.")
                
            print()#line space for terminal aesthetic; better UX

        print("-------- Thank you for using the Distance Converter Application --------")


convert = Converter(None)#initially no value for object 'entry'

convert.main_loop()#this is the executable
