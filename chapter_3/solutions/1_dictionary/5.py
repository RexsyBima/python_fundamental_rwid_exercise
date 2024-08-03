""" 
Exercise 4: Deleting Dictionary Items
- Remove the key-value pair with the key 'Major' from the student dictionary.
- Print the updated student dictionary.
"""

student = {'Name': 'John Doe', 'Age': 20, 'Major': 'Computer Science'}

# Remove the 'Major' key-value pair
del student['Major']

# Print the updated dictionary
print(student)