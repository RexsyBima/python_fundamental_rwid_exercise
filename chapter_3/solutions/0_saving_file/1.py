""" 
Exercise 1: Writing and Saving a Text File
- Define a function called write_to_file that takes two parameters: filename and content. The function should write the content to the file specified by filename.
- Call the write_to_file function with a filename and some content.
"""
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

write_to_file('example.txt', 'This is a sample content.')