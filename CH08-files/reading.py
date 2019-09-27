#chapter 8 reading files
#code opens file and prints it to the screen

with open('hobbies.txt') as hobbies_file:
    contents = hobbies_file.read()
print(contents)