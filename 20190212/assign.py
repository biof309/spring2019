# Assign more than one variable at a time
x = y = z = 1

# Assign more than one variable at a time using tuple unpacking
values = 1, 2, 3
one, two, three = values

# Assign more than one variable at a time from a list comprehension
one, two, three = [x+1 for x in range(3)]

# Assign more than one variable at a time
about_me = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
firstname, lastname, birthyear, birthcity, birthcountry = about_me
first, last, *birth = about_me
first, last, *birth, nationality = about_me

# A string is a sequence of characters
a, b, c = 'a', 'b', 'c'
a, b, c = 'abc'

# Swap two variables
a, b = 'a', 'b'
a, b = b, a
a, b

# Pair up keys and values to make a dictionary
vals = 'Martin', 'Skarzynski', 1985, 'Warsaw', 'Poland'
keys = 'firstname', 'lastname', 'birthyear', 'birthcity', 'birthcountry'
d = dict(zip(keys, vals))

# Unpack two tuples into a list
[*vals, *keys]

# If you want to do something fancy, use a dictionary comprehension
d2 = {'My ' + key: 'is ' + str(value) for key, value in zip(keys, vals)}
d2
