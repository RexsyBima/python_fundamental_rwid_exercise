""" 
Exercise 3: Retry on Exception
- Write a program that repeatedly asks the user to enter a valid number until they enter one correctly.
- Use a try block to convert the input to an integer.
- Use an except block to handle the error if the input is not a valid integer and prompt the user to try agai- n.

"""
while True:
    try:
        user_input = input("Please enter a valid number: ")
        user_number = int(user_input)
        print(f"Thank you for entering the number: {user_number}")
        break  # Exit loop if input is successfully converted to an integer
    except ValueError:
        print("That's not a valid number. Please try again.")
