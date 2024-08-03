""" 
Exercise 3: Reading from a Text File
- Define a function called read_from_file that takes one parameter: filename. The function should read and return the content of the file specified by filename.
- Call the read_from_file function with a filename and print the content of the file.
"""
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

content = read_from_file('example.txt')
print(content)