words = ['Hello', 'good', 'day', 'eh']

#using for loop

count = 0
for word in words:
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

#using .count method

def count_vowels(x):
    count = 0
    for word in x:
        count += (word.count('a') + word.count('e') + 
                  word.count('i') + word.count('o') + word.count('u'))
    print(count)

count_vowels(words)


