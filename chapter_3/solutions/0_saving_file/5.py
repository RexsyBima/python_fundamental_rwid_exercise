""" 
Exercise 5: Reading Lines from a Text File
- Define a function called read_lines_from_file that takes one parameter: filename. The function should read and return the lines of the file specified by filename as a list of strings.
- Call the read_lines_from_file function with a filename and print each line from the list of lines.

"""
def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

lines = read_lines_from_file('example.txt')
for line in lines:
    print(line.strip())