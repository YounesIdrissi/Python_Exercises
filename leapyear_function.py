print("----- Leap Year Tester -----\n")

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter a year: "))
print(is_leap(year))