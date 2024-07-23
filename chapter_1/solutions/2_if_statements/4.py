""" 
4. Grade Classification
   - Ask the user for their grade (0-100) and store it in a variable called grade.
   - Use if statements to classify the grade into categories:
     - 90-100: "A"
     - 80-89: "B"
     - 70-79: "C"
     - 60-69: "D"
     - Below 60: "F"
   - Print the grade category.
"""


grade = int(input("Enter your grade (0-100): "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
