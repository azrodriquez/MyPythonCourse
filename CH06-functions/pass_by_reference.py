def change_first_value(list_to_change):
    '''Changes a list inside a function'''
    #now i want it to randomly pick a number; can i import random in function
    list_to_change[0] = 'something different'

some_nums = [2,6,4,2,22,54,12,8,-1]

#test function by:
# i. print the some_nums list
# ii. call the function passing the list
# iii. print the some_nums list again 

print(some_nums)
change_first_value(some_nums)
print(some_nums)

#this is the result
# [2, 6, 4, 2, 22, 54, 12, 8, -1]
# ['something different', 6, 4, 2, 22, 54, 12, 8, -1]
