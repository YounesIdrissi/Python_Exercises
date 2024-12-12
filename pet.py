#Assignment: Classes and Objects accessor and mutator methods

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    #mutator/set methods
    def set_name(self):
        self.__name = input("Enter a name: ")

    def set_animal_type(self):
        self.__animal_type = input("Enter an animal type: ")

    def set_age(self):
        self.__age = input("Enter an age: ")

    #accessor/get methods
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

#object attributes are subject to change
my_pet = Pet("placeholder", "placeholder", "placeholder") #object instantiated

my_pet.set_name()
my_pet.set_animal_type()
my_pet.set_age()

print(f"Name: {my_pet.get_name()}")
print(f"Animal type: {my_pet.get_animal_type()}")
print(f"Age: {my_pet.get_age()}")
print(f"{my_pet.get_name()} the {my_pet.get_animal_type()} is {my_pet.get_age()} years old!")