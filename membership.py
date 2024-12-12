#gym membership fee calculator

def membership_fee():
    age = int(input("Enter your age: "))
    while age < 0:
        age = int(input("Age can't be negative! Enter your age: "))
        
    length = int(input("Enter the length of your membership in months (1, 3, 6, or 12): "))
    while length < 0:
        length = int(input("Length of membership can't be negative! Enter the length of your membership in months (1, 3, 6, or 12): "))
        
    else:
        if age >= 5 and age <= 12:
            if length == 1:
                print("Your membership fee is $40")
            elif length == 3:
                print("Your membership fee is $110")
            elif length == 6:
                print("Your membership fee is $220")
            elif length == 12:
                print("Your membership fee is $450")
            else:
                print("Invalid length of membership!")
        elif age >= 13 and age <= 26:
            if length == 1:
                print("Your membership fee is $50")
            elif length == 3:
                print("Your membership fee is $140")
            elif length == 6:
                print("Your membership fee is $280")
            elif length == 12:
                print("Your membership fee is $550")
            else:
                print("Invalid length of membership!")
        elif age >= 27 and age <= 55:
            if length == 1:
                print("Your membership fee is $60")
            elif length == 3:
                print("Your membership fee is $170")
            elif length == 6:
                print("Your membership fee is $340")
            elif length == 12:
                print("Your membership fee is $650")
            else:
                print("Invalid length of membership!")
        elif age >= 56 and age <= 100:
            if length == 1:
                print("Your membership fee is $30")
            elif length == 3:
                print("Your membership fee is $80")
            elif length == 6:
                print("Your membership fee is $160")
            elif length == 12:
                print("Your membership fee is $250")
            else:
                print("Invalid length of membership!")
        else:
            print("You are either too young or too old to have a gym membership!")

membership_fee()




