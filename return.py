def foo1(v):
    v+=1
    return v

def foo2():
    val = 10
    print(foo1(val))
    print(val)#val does NOT get updated through external functions.

foo2()

'''
Notice how the functions do not share the object 'val'. When it comes to scope, the 
functions cannot see inside each other. When 'val' is passed as an argument to foo1,
it creates a new object which is no longer associated to the original object 'val'.
Returning the argument simply returns the value of the new object.
'''