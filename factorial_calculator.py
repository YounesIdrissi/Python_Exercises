
num = int(input("Enter a number to factorialize: "))

if num == 0 or num == 1:
    factorial = 1
else:
    factorial = int(num * (num - 1))
    num -= 1
    while num > 1:
        factorial *= (num - 1)
        num -= 1
    
print(factorial)