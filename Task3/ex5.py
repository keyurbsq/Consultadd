# Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

mylist = [4, 5, 3, 9, 1, 2]

result = []
for x in mylist:
    if x % 2 != 0:
        result.append(x)

print(result)
