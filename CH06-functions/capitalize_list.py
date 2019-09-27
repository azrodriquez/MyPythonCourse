#bonus chapter 6

def capitalize_list(words):
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        print(words)


fruits = ('apple', 'banana', 'pear', 'pineapple', 'blueberry')
print(fruits)
capitalize_list(fruits)
print(fruits)   