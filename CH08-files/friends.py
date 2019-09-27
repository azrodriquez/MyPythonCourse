#chapter 8 reading files BONUS MATERIAL: READ IN FRIENDS
#code opens specific file and prints line contents to the screen

with open('friends.txt') as friends_file:
    contents = str(friends_file.read(),rt)
    for line in contents:
        print()
    print(contents)

