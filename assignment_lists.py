#Assignment: Lists

#task 1
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

#task 2
print(my_list[2])

#task 3
print(my_list[-1])

#task 4
new_list = my_list[1:4]
print(new_list)

#task 5
def count_vowels(x):
    count = 0
    for word in x:
        for letter in word:
            if letter == 'a':
                count += 1
            elif letter == 'e':
                count += 1
            elif letter == 'i':
                count += 1
            elif letter == 'o':
                count += 1
            elif letter == 'u':
                count += 1
    print(count)

count_vowels(my_list)

#task 6
def reverse_list(x):
    x.reverse()
    print(x)
    
reverse_list(my_list)

#task 7
dup_list = ['car', 'car', 'suv', 'truck', 'motorcycle', 'suv']
def remove_duplicates(x):
    rmv_dup = []
    for word in x:
        if word not in rmv_dup:
            rmv_dup.append(word)

    return rmv_dup

print(remove_duplicates(dup_list))

#task 8
list_1 = [1, 3, 4, 6, 8, 9, 10] #4, 6, 8, 10 are not in 2nd list
list_2 = [1, 2, 3, 5, 7, 9, 11]
def remove_items(x, y):
    not_in_second = []
    for item in x:
        if item not in y:
            not_in_second.append(item)
        
    return not_in_second

print(remove_items(list_1, list_2))
