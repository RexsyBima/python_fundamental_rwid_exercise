""" 
Exercise 4: Writing Multiple Lines to a Text File
- Define a function called write_lines_to_file that takes two parameters: filename and lines. The lines parameter should be a list of strings, each representing a line of text. The function should write each line to the file specified by filename, with each line on a new line.
- Call the write_lines_to_file function with a filename and a list of lines.
"""
def write_lines_to_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

lines = ['First line', 'Second line', 'Third line']
write_lines_to_file('example.txt', lines)
