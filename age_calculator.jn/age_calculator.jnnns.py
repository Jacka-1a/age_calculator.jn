import os
repeat = "yes"
while repeat == "yes":
    # Get the user to input their name
    name = input("Enter your name: ").strip()

    # Get the user to input their birth year
    birthday_year = int(input("Enter your birth year: ").strip())

    # Get the user to enter the current year
    current_year = int(input("Enter the current year: ").strip())

    # Ask the user if they have had their birthday yet
    birthday = input("Have you had your birthday yet? (yes/no): ").lower().strip()

    age = current_year - birthday_year

    print("Your name is", name)

    if birthday == "no":
        age = age - 1

    print(f"Your age is: {age}")

    repeat = input("Would you like to run the program again? (yes/no): ").lower().strip()
    os.system('cls||clear')
print("Thank you for using the age calculator.")

