""" 
Exercise 2: Check Membership in a String
Create a string called sentence with the value "Python programming is fun".
Ask the user to enter a word.
Use the in operator to check if the entered word is in the sentence.
Print an appropriate message.
"""
sentence = "Python programming is fun"
user_word = input("Enter a word: ")
if user_word in sentence:
    print("The word is in the sentence.")
else:
    print("The word is not in the sentence.")
