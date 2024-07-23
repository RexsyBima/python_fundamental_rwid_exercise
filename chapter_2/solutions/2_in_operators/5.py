""" 
Exercise 5: Check Substring in a String
Create a string called text with the value "Hello, welcome to Python programming!".
Ask the user to enter a substring.
Use the in operator to check if the entered substring is in the text.
Print an appropriate message.

"""

text = "Hello, welcome to Python programming!"
substring = input("Enter a substring: ")

if substring in text:
    print("The substring is in the text.")
else:
    print("The substring is not in the text.")
    
