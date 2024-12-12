#Practice Object Oriented Programming
class AlgebraFunctions:
    def __init__(self, init_message):
        self.this_can_literally_be_anything = init_message
        print(init_message)

    print("The following are the y-values to the x_values passed as arguments: \n") #why is this outputed first???

    def x_squared(self, x):
        print(x**2)
    def etothex(self, x):
        print(2.71**x)
    def one_overx(self, x):
        print(1/x)

'''
An object is an instance of a class // The instantiation of a class is an object

btw this is a multiline comment
'''
y = AlgebraFunctions("Class 'AlgebraFunctions' has been initialized") #This is an instance of the above class
#note that arguments passed here go to the initialization method (init)


y.x_squared(2) #Plug in the argument (x-value) to recieve the result (y-value)
y.etothex(4) 
y.one_overx(8)
