""" 
2. Even or Odd
   - Ask the user for a number and store it in a variable called number.
   - Use an if statement to check if the number is even or odd.
   - Print "The number is even." if it is even, and "The number is odd." if it is odd.
"""


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
