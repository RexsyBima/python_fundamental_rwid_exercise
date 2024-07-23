""" 
Exercise 6: List Comprehensions
- Create a list called numbers with the elements: 1, 2, 3, 4, 5.
- Use a list comprehension to create a new list called squares that contains the squares of each number in numbers.
- Print the squares list.
"""


numbers = [1, 2, 3, 4, 5]

squares = [num**2 for num in numbers]

print(squares)
