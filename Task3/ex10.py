#Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which
# contains every number in the form of string.

n = input('Please enter comma separated numbers:')

lst = n.split(',')
t = tuple(lst)

print(lst, t)
