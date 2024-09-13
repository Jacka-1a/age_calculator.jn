#'''
#print(sports)
#print(type(sports))
#print(len(sports))
#print(sports[0])
#print(sports[-1])
#print(sports[-2])
#print(sports[0:3])
#print(type(sports[0]))
#print(type(sports[1]))
#print(type(sports[2]))
#print(type(sports[3]))
#'''
#for sport in sports:
 #   print(type(sport))
#   print(sport)
repeat = "yes"
sports = ["Basketball"]  # Empty list.
while repeat == "yes":
    new_sport = input("Add your favourite sport: ")
    if new_sport:
        sports.append(new_sport)
        print("Updated sports list: ", sports)
    else:
        print("No new sport added.")
        print("Sports List:", sports)
    for i, sport in enumerate(sports):# loop through sports list with index.
        print(f"Sport {i+1}: {sport}")
    repeat = input("Would you like to run the program again? (yes/no): ").lower().strip()
print("Exiting the program.") # Print a message when the user exits the program.