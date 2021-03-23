# Write a program in Python to find out the character in a string which is uppercase using list comprehension

input_str = "Hello..How Are You?"

res = [char for char in input_str if char.isupper()]

print("Uppercase characters in string: " + str(res))