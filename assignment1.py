# Date: 9/18/24 
# Description: Ask the user to enter the hours and rate for an employee,
# then calculate and display the grossPay and netPay. 
# Assume that there is 25% Tax deduction.

hours=float(input("Enter total hours worked per week: \n"))
rate=float(input("Enter pay rate per hour: \n"))

float=total_hours = hours*52
float=gross_pay = total_hours*rate
float=net_pay = gross_pay*0.75

print("\nGross pay: $",gross_pay)
print("Net pay: $",net_pay)

