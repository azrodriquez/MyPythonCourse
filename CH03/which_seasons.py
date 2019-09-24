print('Welcome to the which season program')

month_string = input('Input the month number (e.g. January==1): ')
day_string = input('Input the day of the month (e.g. 19): ')

month = int(month_string)
day = int(day_string)

if month == 1 or month == 2 or month == 3:
    season = 'winter'
elif month ==4 or month == 5 or month == 6:
    season = 'spring'
elif month == 7 or month == 8 or month == 9:
    season = 'summer'
else:
    season = 'autumn'


if (month == 3) and (day > 19):
    season = 'spring'
elif (month == 6) and (day < 20):
    season = 'summer'
elif (month == 9) and (day > 21):
    season = 'autumn'
elif (month == 12) and (day > 20):
    season = 'winter'

print("Season is ", season)

#BONUS MATERIAL

print(input("What is your favorite month? (e.g. May == 5)"))

if (month == 9):
    print("September is my favorite too")
elif (month > 9):
    print("Those are nice too, but cold")
elif (month < 9):
    print("Winter, Spring and Summer are great")
else:
    print("That's not a month i know of...")