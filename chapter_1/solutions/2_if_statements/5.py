""" 
5. Login System
   - Ask the user for a username and password.
   - Check if the username is "admin" and the password is "password123".
   - If both are correct, print "Login successful."
   - If either is incorrect, print "Login failed."
   - Bonus: Add a confirm password feature, so if the password and confirm password are equal, then login.
"""


username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password123":
    print("Login successful.")
else:
    print("Login failed.")

# Bonus: Add confirm password feature
confirm_password = input("Enter your password again: ")
if password == confirm_password:
    print("Login successful.")
else:
    print("Login failed. Passwords do not match.")
