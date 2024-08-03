""" 
Exercise 6: Iterating Through a Dictionary
- Using a for loop, iterate through the student dictionary and print each key and value pair in the format "key: value".
"""

student = {'Name': 'John Doe', 'Age': 20, 'Major': 'Computer Science'}

# Iterate through the dictionary
for key, value in student.items():
    print(f'{key}: {value}')