""" 
Exercise 8: Nested Dictionaries
- Create a dictionary called classroom with the following nested dictionaries:
    Student1: {'Name': 'Alice', 'Age': 22, 'Major': 'Mathematics'}
    Student2: {'Name': 'Bob', 'Age': 24, 'Major': 'Physics'}
- Print the classroom dictionary.
- Print the 'Major' of student1
- Print the 'Age' of student 2
"""

classroom = {
    'Student1': {'Name': 'Alice', 'Age': 22, 'Major': 'Mathematics'},
    'Student2': {'Name': 'Bob', 'Age': 24, 'Major': 'Physics'}
}

print(classroom)

print(classroom['Student1']['Major'])
print(classroom['Student2']['Age'])