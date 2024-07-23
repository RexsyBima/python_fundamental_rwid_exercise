""" 
Exercise 3: Age Calculation
- Ask the user for the current year and store it in a variable called current_year.
- Ask the user for their birth year and store it in a variable called birth_year.
- Convert the input strings to integers.
- Calculate the user's age and print it.
"""

current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print("You are", age, "years old.")
