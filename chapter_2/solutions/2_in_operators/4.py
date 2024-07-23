""" 
Exercise 4: Check Membership in a Set
Create a set of numbers called numbers with the elements: 1, 2, 3, 4, 5.
Ask the user to enter a number.
Use the in operator to check if the entered number is in the numbers set.
Print an appropriate message.
"""
numbers = {1, 2, 3, 4, 5}

user_number = int(input("Enter a number: "))
if user_number in numbers:
    print(f"The number {user_number} is in the set.")
else:
    print(f"The number {user_number} is not in the set.")
