""" 
Exercise 5: Boolean Conversion
1. Create a variable called true_str and assign the string "True" to it.
2. Create a variable called false_str and assign the string "False" to it.
3. Convert true_str and false_str to their respective boolean values and print the results.
4. Create a variable called num and assign it any non-zero integer value. Convert num to a boolean and print the result.

"""


# Exercise 5: Boolean Conversion try except
true_str = "True"
false_str = "False"

try:
    true_bool = bool(true_str)
    print(true_bool)
except ValueError:
    print("Invalid input. Please enter a valid boolean string.")

try:
    false_bool = bool(false_str)
    print(false_bool)
except ValueError:
    print("Invalid input. Please enter a valid boolean string.")

num = 123
try:
    num_bool = bool(num)
    print(num_bool)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
