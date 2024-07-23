""" 
Exercise 4: Logical Comparisons
- Ask the user for their age and store it in a variable called age.
- Use boolean expressions to check if:
    - The age is between 13 and 19 (inclusive) (i.e., a teenager).
    - The age is 65 or older (i.e., a senior citizen).
- Print appropriate messages for each case.
"""

age = int(input("Enter your age: "))

teenager = age >= 13 and age <= 19
senior_citizen = age >= 65

if teenager:
    print("You are a teenager.")
elif senior_citizen:
    print("You are a senior citizen.")
else:
    print("You are not a teenager or a senior citizen.")
