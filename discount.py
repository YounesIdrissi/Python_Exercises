#Date: 9/25/24
#Shopping Discount Calculator

original_price = float(input("Enter the original price of the item: "))
customer_type = input("Are you a regular or premium customer? ")

if customer_type == 'regular':
    if original_price > 100:
        final_price = original_price * 0.90
        print(f"Your original price, ${original_price}, has a 10% discount applied. Your final price is: ${final_price}")
    elif 50 <= original_price <= 100:
        final_price = original_price * 0.95
        print(f"Your original price, ${original_price}, has a 5% discount applied. Your final price is: ${final_price}")
    elif original_price < 50:
        print(f"Your original price, ${original_price}, has a no discount applied. Your final price is: ${original_price}")
    else:
        print(f"{original_price} is not a valid price")

elif customer_type == 'premium':
    if original_price > 100:
        final_price = original_price * 0.80
        print(f"Your original price, ${original_price}, has a 20% discount applied. Your final price is: ${final_price}")
    elif 50 <= original_price <= 100:
        final_price = original_price * 0.90
        print(f"Your original price, ${original_price}, has a 10% discount applied. Your final price is: ${final_price}")
    elif original_price < 50:
        final_price = original_price * 0.95
        print(f"Your original price, ${original_price}, has a 5% discount applied. Your final price is: ${final_price}")
    else:
        print(f"{original_price} is not a valid price")

else:
    print(f"{customer_type} is not a valid customer type")