#Lab: Lists

#Task 1
my_list = []
fruit_list = ['apple', 'banana', 'cherry']
num_list = [1, 2, 3, 4]

print(my_list)
print(fruit_list)
print(num_list)

#Task 2
second_fruit = fruit_list[1]
print(second_fruit)
third_num = num_list[2]
print(third_num)
last_fruit = fruit_list[-1]
print(last_fruit)

#Task 3
fruit_list.append('orange')
fruit_list.insert(1, 'grape')
fruit_list.remove('apple')
fruit_list.remove('cherry')
num_list.reverse()
print(fruit_list)
print(num_list)

#Task 4
random_numbers = [5, 2, 8, 1, 3]
random_numbers.sort()
random_numbers.reverse()
print(random_numbers)

#Task 5
list_1 = ['a', 'b', 'c']
list_2 = ['d', 'e', 'f']
combined = list_1 + list_2
print(combined)
repeated = list_1 * 3
print(repeated)

