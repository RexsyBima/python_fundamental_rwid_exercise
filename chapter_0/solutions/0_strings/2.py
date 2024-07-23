""" 
Exercise 2: String Concatenation
1. Create a variable called first_name and assign your first name to it.
2. Create a variable called last_name and assign your last name to it.
3. Concatenate first_name and last_name to create a new variable called full_name.
4. Print the value of full_name.
bonus :
    Concatenate the first_name and last_name into a new variable but with f string
"""

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

# Bonus
full_name_f_string = f"{first_name} {last_name}"
print(full_name_f_string)
