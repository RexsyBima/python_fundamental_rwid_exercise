""" 
3. Positive, Negative, or Zero
   - Ask the user for a number and store it in a variable called number.
   - Use an if statement to check if the number is positive, negative, or zero.
   - Print an appropriate message for each case.
"""


number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

