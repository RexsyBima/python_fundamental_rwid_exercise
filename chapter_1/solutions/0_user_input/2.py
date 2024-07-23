""" 
Exercise 2: Simple Calculator
- Ask the user for two numbers and store them in variables num1 and num2.
- Convert the input strings to floats.
- Perform addition, subtraction, multiplication, and division on the two numbers.
- Print the results of each operation.
"""

# Ask the user for two numbers and store them in variables num1 and num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform addition, subtraction, multiplication, and division
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print the results of each operation
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
