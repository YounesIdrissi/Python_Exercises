#Date:9/27/24
#Assignment: Python Loops Temp C to F Converter

fahrenheit = 0.0
total_fahrenheit = 0.0
count = 0
average = 0.0

celsius = float(input("Enter temperature in Celsius (enter negative number to stop): "))

while celsius >= 0:
    fahrenheit = (celsius * 9/5) + 32
    count += 1
    total_fahrenheit += fahrenheit
    average = total_fahrenheit / count
    print(f"{celsius} degrees Celsius converts to {fahrenheit} degrees Fahrenheit.")
    print(f"Total Fahrenheit temperature: {total_fahrenheit} degrees")
    print(f"Total count: {count}")
    celsius = float(input("Enter temperature in Celsius (enter negative number to stop): "))

print(f"Total Fahrenheit temperature: {total_fahrenheit} degrees")
print(f"Total count: {count}")
print(f"Average Fahrenheit temperature: {average} degrees")

# updated temp convertor 10/14/24:


#total_temp = 0
#count = 0
#celcius = float(input("Enter temperature in celcius: "))

#while celcius >= 0:
#    count += 1
#    fahrenheit = (celcius * 9 / 5) + 32
#    total_temp += fahrenheit
#    print(f"{celcius} degrees celcius is {fahrenheit} degrees fahrenheit")
#    celcius = float(input("Enter temperature in celcius (neg to stop): "))

#avg_temp = total_temp / count
#print(f"The average temperature is {avg_temp} degrees fahrenheit")