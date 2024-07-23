""" 
Exercise 6: Check Multiple Memberships
Create a list of fruits called fruits with the elements: "apple", "banana", "cherry".
Ask the user to enter a fruit.
Use the in operator to check if the entered fruit is in the fruits list and if "banana" is also in the list.
Print an appropriate message.
"""

fruits = ["apple", "banana", "cherry"]
fruit = input("Enter a fruit: ")

if fruit in fruits and "banana" in fruits:
    print(f"{fruit} and 'banana' are both in the list.")
elif fruit in fruits:
    print(f"{fruit} is in the list.")
elif "banana" in fruits:
    print("'banana' is in the list.")
else:
    print("None of the fruits are in the list.")
