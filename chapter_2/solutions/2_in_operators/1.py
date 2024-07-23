""" 
Exercise 1: Check Membership in a List
- Create a list of colors called colors with the elements: "red", "green", "blue".
- Ask the user to enter a color.
- Use the in operator to check if the entered color is in the colors list.
- Print an appropriate message.
"""


colors = ["red", "green", "blue"]
color = input("Enter a color: ")

if color in colors:
    print(f"{color} is in the colors list.")
else:
    print(f"{color} is not in the colors list.")
