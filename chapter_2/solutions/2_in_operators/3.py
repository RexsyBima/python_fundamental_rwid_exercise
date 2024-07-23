""" 
Exercise 3: Check Membership in a Dictionary
Create a dictionary called students with the following key-value pairs: "Alice": 85, "Bob": 90, "Charlie": 78.
Ask the user to enter a name.
Use the in operator to check if the entered name is a key in the students dictionary.
Print an appropriate message.
"""

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
name = input("Enter a name: ")
if name in students:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")
