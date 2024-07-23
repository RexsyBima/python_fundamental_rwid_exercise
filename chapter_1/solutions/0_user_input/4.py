""" 
Exercise 4: Temperature Converter
- Ask the user for a temperature in Celsius and store it in a variable called celsius.
- Convert the input string to a float.
- Convert the temperature to Fahrenheit using the formula.
- Print the temperature in Fahrenheit.
"""


celsius = input("Enter temperature in Celsius: ")
celsius = float(celsius)
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
