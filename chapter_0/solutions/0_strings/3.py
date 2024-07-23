""" 
Exercise 3: String Methods
1. Create a variable called greeting and assign the string "Hello, World!" to it.
2. Convert the string to all uppercase letters and print it.
3. Convert the string to all lowercase letters and print it.
4. Find the length of the string and print it.
5. Replace the word "World" with your name and print the result.
"""

greeting = "Hello, World!"

# Convert to all uppercase
print(greeting.upper())

# Convert to all lowercase
print(greeting.lower())

# Find the length of the string
print(len(greeting))

# Replace the word "World" with your name
your_name = "John"
print(greeting.replace("World", your_name))
