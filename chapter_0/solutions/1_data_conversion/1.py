""" 
Exercise 1: Basic Data Conversion
1. Create a variable called num_str and assign the string "123" to it.
2. Convert num_str to an integer and store the result in a variable called num_int.
3. Convert num_str to a float and store the result in a variable called num_float.
4. Print num_int and num_float.
"""

num_str = "123"
try:
    num_int = int(num_str)
    num_float = float(num_str)
    print(num_int)
    print(num_float)
except ValueError:
    print("Invalid input. Please enter a valid number.")
