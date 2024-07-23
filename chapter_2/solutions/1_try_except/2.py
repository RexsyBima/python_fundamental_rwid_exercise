""" 
Exercise 2: Division with Exception Handling
- Write a program that asks the user to enter two numbers.
- Use a try block to divide the first number by the second.
- Use two except blocks to handle the errors if the second number is zero or if either input is not a valid number.
- Print appropriate messages for each case.
"""


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: One or both of the inputs are not valid numbers.")
