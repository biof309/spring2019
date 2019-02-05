# To run a line of code in PyCharm, press alt+shift+E
# To run a code cell in PyCharm, press ctrl+enter
# To run a code cell in VS code, press shift+enter
# To assign a variable, run variable_name = value
x = 2
# Assign two variables the same value
y = x = 5
# Assign multiple variables at once
z = 1, 2, 3 # z is a tuple, this is a sequence of values
one, two, three = 1, 2, 3
zero, one, two = range(3)
# x is an int
x = 5
# y and z are floats
y = 1/3
z = 5.
# Replace my name with your name below
name = "Martin"
five = str(x)
help(range)
# Instead of the help function, use quick documentation in PyCharm
# Check the type
# Types we use today: int, str, float, list, tuple
type(5.)

# List comprehension
[chr(65+i) for i in range(26)]
# Assign multiple variables using a list comprehension
one, two, three = [y*y for y in range(3)]
