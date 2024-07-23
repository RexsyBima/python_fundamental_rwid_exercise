""" 
Exercise 4: String to Float Conversion with Error Handling
1. Create a variable called price_str and assign the string "19.99" to it.
2. Convert price_str to a float and store the result in a variable called price_float.
3. Print price_float.
4. Try converting a string that is not a valid float (e.g., "abc") to a float and handle the error gracefully using a try-except block.

"""

price_str = "19.99"
try:
    price_float = float(price_str)
    print(price_float)
except ValueError:
    print("Invalid input. Please enter a valid number.")
