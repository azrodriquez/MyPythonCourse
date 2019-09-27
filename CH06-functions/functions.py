def print_stars(count = 10):
    print("*"*count)

print_stars()
print_stars(20)

def slice_list(list_to_slice, upper_bound):
    """Returns slice of list if upper bound is valid"""
    if (len(list_to_slice) > upper_bound):
        print('Slicing...')
        return list_to_slice[:upper_bound]
    else:
        print('Value too high...', upper_bound)
        return None

some_nums = [2,6,4,2,22,54,12,8,-1]

print('Value returned ', slice_list(some_nums, 4))

print(slice_list(some_nums, 4))
print(slice_list(some_nums, 12))
print(slice_list(some_nums, 20))

#error if no () at end of function
#   File ".\functions.py", line 1
#     def print_stars:
#                    ^
# SyntaxError: invalid syntax

# error with print_stars(20) 
# Traceback (most recent call last):
#   File ".\functions.py", line 5, in <module>
#     print_stars(20)
# TypeError: print_stars() takes 0 positional arguments but 1 was given


#adding print(slice_list(some_nums, 20))
# **********
# ********************
# Slicing...
# Value returned  [2, 6, 4, 2]
# Slicing...
# [2, 6, 4, 2]
# Value too high... 12
# None
# Value too high... 20
# None