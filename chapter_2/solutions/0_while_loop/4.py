""" 
Exercise 4: Password Validation
-Ask the user to enter a password.
-Use a while loop to keep asking for the password until the user enters "password123".
-Print "Access granted" when the correct password is entered.
"""

password = ""
while password != "password123":
    password = input("Enter your password: ")

print("Access granted.")
