""" 
Exercise 2: Float to Integer Conversion
1. Create a variable called num_float and assign the float 456.789 to it.
2. Convert num_float to an integer and store the result in a variable called num_int.
3. Print num_int and observe what happens to the decimal part
"""

num_float = 456.789
try:
    num_int = int(num_float)
    print(num_int)
except ValueError:
    print("Invalid input. Please enter a valid number.")
