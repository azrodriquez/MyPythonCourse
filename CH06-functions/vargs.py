# def print_stars(count = 10):
#     print("*"*count)

# print_stars()
# print_stars(20)

def slice_list(list_to_slice, *upper_bounds):
    """Returns one list of results for all bounds passed in"""
    list_to_return = []
    for upper_bound in upper_bounds:
        if (len(list_to_slice) > upper_bound):
            print('Slicing...') 
            list_to_return.append(list_to_slice[:upper_bound])
        else:
            list_to_return.append(None)
    return list_to_return

some_nums = [2,6,4,2,22,54,12,8,-1]

print('Value returned ', slice_list(some_nums, 4))

print(slice_list(some_nums, 4))
print(slice_list(some_nums, 12))
print(slice_list(some_nums, 20))
print(slice_list(some_nums, 4,12,2,3))


# this is the output of adding line 25 print(slice_list(some_nums, 4,12,2,3))
# **********
# ********************
# Slicing...
# Value returned  [[2, 6, 4, 2]]
# Slicing...
# [[2, 6, 4, 2]]
# [None]
# [None]
# Slicing...
# Slicing...
# Slicing...
# [[2, 6, 4, 2], None, [2, 6], [2, 6, 4]]