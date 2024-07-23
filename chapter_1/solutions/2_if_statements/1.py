""" 
1. Basic If Statement
   - Ask the user for their age and store it in a variable called age.
   - If the user is 18 or older, print "You are an adult."
   - If the user is younger than 18, print "You are a minor."
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
