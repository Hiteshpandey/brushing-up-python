"""
Python allows us to save and return multiple values at a time by separating them by comma
"""
# multiple variables assigning
coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# Instead we can do tis
x, y, z = coordinates
print(x, y, z)

# Same with list

coordinates = [1, 2, 3]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# Instead we can do tis
x, y, z = coordinates
print(x, y, z)

# Multi assignment
a, b, c = 1, 'z', [1, 2, 3]
print(a, b, c)