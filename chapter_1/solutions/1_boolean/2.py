""" 
Exercise 2: Boolean Expressions
 - Ask the user for two numbers, num1 and num2.
 - Create and print the following boolean expressions:
    - num1 is greater than num2
    - num1 is equal to num2
    - num1 is less than or equal to num2
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} <= {num2} : {num1 <= num2}")
