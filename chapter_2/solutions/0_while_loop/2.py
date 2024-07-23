""" 
Exercise 2: Sum of Numbers
-Ask the user for a positive integer n.
-Use a while loop to calculate the sum of all numbers from 1 to n.
-Print the sum.
"""
n = int(input("Enter a positive integer: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of all numbers from 1 to", n, "is", sum)
