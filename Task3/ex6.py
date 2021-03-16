# Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and 30 (both included).

mylist = []
for x in range(1, 31):
    if x < 6 or x > 25:
        mylist.append(x ** 2)

print(mylist)
