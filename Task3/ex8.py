# Create a new dictionary by concatenating the following two dictionaries:

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {}

c.update(a)
c.update(b)

print(c)