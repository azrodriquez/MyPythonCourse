import sys

#get file name

program_name = sys.argv[0]
print('original name\t\t', program_name)
print('uppercase\t\t', program_name.upper())
print('original name\t\t', program_name)

#replace underscore with space
program_name = program_name.replace('_', ' ')
print('removed underscore\t', program_name)

#replace .\ if it exists
program_name = program_name.replace('.\\', '  ')
print('removed .\\\t\t', program_name)

#replace .py if exists
program_name = program_name.replace('.py', '')
print('removed .py\t\t', program_name)

#upper
program_name = program_name.upper()
print('upper\t\t\t', program_name)

#create welcome message
welcome_message = 'Welcome to {}'
welcome_message = welcome_message.format(program_name)
print(welcome_message)

#use center to display
print('length is', len(program_name))
welcome_message = welcome_message.center(len(welcome_message)*3, '*')
print(welcome_message)

#ask user for numeric value
good_year = False
movie = input("What is your favorite movie? ")
print(movie)
while not good_year:
    year = input("What year is your favorite movie from? ")
    if (year.isdecimal()):
        good_year = True
    else:
        print("Please enter a valid year...")

#use str.format
movie = movie.strip()
print(movie)

message = "In {}, the movie {} debuted"
print(message.format(year, movie))