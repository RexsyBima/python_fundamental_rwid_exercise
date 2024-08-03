""" 
Exercise 7: Checking for Keys in a Dictionary
- Check if the key 'Name' exists in the student dictionary. Print "Key exists" if it does, otherwise print "Key does not exist".
- Check if the key 'Major' exists in the student dictionary. Print "Key exists" if it does, otherwise print "Key does not exist".
"""
student = {'Name': 'John Doe', 'Age': 20, 'Major': 'Computer Science'}

# Check for 'Name' key
if 'Name' in student:
    print('Key exists')
else:
    print('Key does not exist')

# Check for 'Major' key
if 'Major' in student:
    print('Key exists')
else:
    print('Key does not exist')