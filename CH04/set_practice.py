#this is exercise 1
# num_set = {2,6,4,2,22,54,12,18,-1}

# print(num_set)
# print(len(num_set))


#this is exercise 2
# import random

# name_list = ['adam', 'barry', 'doug', 'cathy', 'ellen']

# volunteers = set(random.sample(name_list,3))
# qualified = set(random.sample(name_list,3))
# new_team = volunteers.intersection(qualified)

# print('volunteers are: ', volunteers)
# print('qualified are: ', qualified)
# print('volunteering and qualified', new_team)


#BONUS MATERIAL
#create variable vowel set
vowels = {'a', 'e', 'i', 'o','u'}
#create variable words list
words = ['alligator', 'penguin', 'water fowl', 'giraffe']

# need to loop through the word list by letter for vowels
# for each word that has a vowel print out
# the word and how many vowels the word has
for word in words:
    counter = 0
    for letter in vowels:
        if letter in vowels:
            counter += 1
    print(f'the word {word} has {counter} vowels')