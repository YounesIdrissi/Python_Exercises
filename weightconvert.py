print("Weight Converter:\n")
unit = input("Enter lb or kg: ")
weight = float(input("Enter the weight: "))

if unit == "lb":
    convertion = weight / 2.2
    print(f"{weight}lbs converts to {round(convertion, 1)}kgs")
elif unit == "kg":
    convertion = weight * 2.2
    print(f"{weight}kgs converts to {round(convertion, 1)}lbs")
else:
    print(f"{unit} is not a valid unit of weight")
