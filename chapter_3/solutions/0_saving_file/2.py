""" 
Exercise 2: Appending to a Text File
- Define a function called append_to_file that takes two parameters: filename and content. The function should append the content to the file specified by filename.
- Call the append_to_file function with a filename and some content to append.
clue = https://www.geeksforgeeks.org/python-append-to-a-file/

"""
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

append_to_file('example.txt', '\nThis content is appended.')