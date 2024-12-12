string1 = "Programming"
string2=" Languages"

print('The length of string 1 is:',len(string1))
print('Concatenation:',string1+string2)
print('Slicing: '+string1[3:7])
print('gram' in string1) #is Gram substring in the string 1?'
print(string2.isdigit()) # checking if string 2 is numbers only
print(string1.upper()) # convert string 1 to upper case
print("the substring 'gram' is found at string 1 at position:"
      +str(string1.find('gram')))
print("Replace the substring 'gram' in at string with ounces:"
      +str(string1.replace('gram','ounces')))