""" 
Exercise 1: Basic Try-Except
- Write a program that asks the user to enter a number.
- Use a try block to convert the input to an integer.
- Use an except block to handle the error if the input is not a valid integer.
- Print an appropriate message in both cases.
"""

number = input("Enter a number: ")

try:
    number_int = int(number)
    print(f"The number {number} has been converted to {number_int}.")
except ValueError:
    print(f"The input {number} is not a valid integer.")
