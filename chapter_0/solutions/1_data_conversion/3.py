""" 
Exercise 3: Integer to String Conversion
Create a variable called age and assign your age to it as an integer.
Convert age to a string and store the result in a variable called age_str.
Print a sentence that says "I am [age] years old." using the age_str variable.

"""

try:
    age = int(input("Enter your age: "))
    age_str = str(age)
    print(f"I am {age_str} years old.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
