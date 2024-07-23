""" 
Exercise 6: List to String Conversion
Create a list called fruits with the following elements: "apple", "banana", and "cherry".
Convert the list to a string where the elements are joined by commas, and store the result in a variable called fruits_str.
Print fruits_str.
"""

fruits = ["apple", "banana", "cherry"]
try:
    fruits_str = ", ".join(fruits)
    print(fruits_str)
except TypeError:
    print("Invalid input. Please enter a valid list.")
