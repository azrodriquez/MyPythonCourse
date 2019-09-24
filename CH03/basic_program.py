# step 2
keep_looping = True
# Step 3, 4, 5
while keep_looping:
    month = int(input("Enter a month numerically: "))
    day = int(input("Enter a day numerically: "))
    if (month > 0 and month < 13 and day > 0 and day <= 31):
        keep_looping = False
    else:
        print('Invalid entries. Enter 1-12 for month, enter 1-31 for days')
        
print("You did it")