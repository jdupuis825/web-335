#-----------------------------------------
# Title: dupuis_hobbies.py
# Author: Jocelyn Dupuis
# Date: 09/06/2023
# Description: Python file for hobbies exercise 5.3
#-----------------------------------------

# Create a list of hobbies
hobbies = ['Music', 'Travel', 'Concerts', 'Cooking', 'Family time', 'Exercise']

# Create a list of days
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Print hobbies
print('I love')
for hobby in hobbies:
    print("- " + hobby)

# for loop and if/else statement to print messages for each day
print("\nDay of the week:")
for day in days:
    if day == "Sunday" or day == "Saturday":
        print(f"{day}: It's your day off, time to enjoy your hobbies!")
    else:
        print(f"{day}: It's a work day, time to focus!")

        
