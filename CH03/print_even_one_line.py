counter = 0
while counter < 20:
    if counter %2 == 0:
        print(counter)
    counter += 1
print("Finished Looping") 


counter = 0
while counter < 20:
    if counter %2 == 0:
        print(counter, end="")
    counter += 1
print("\n", "Finished Looping") 


counter = 0
while counter < 20:
    if counter %2 == 0:
        print(counter, end=" ")
    counter += 1
print("\n", "Finished Looping") 
