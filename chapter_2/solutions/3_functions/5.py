""" 
Exercise 5: Default Parameter Values
 - Define a function called greet that takes a name as a parameter and prints "Hello, [name]!".
 - Set the default value of the name parameter to "Guest".
 - Call the greet function without arguments and with an argument.

"""


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Alice")