from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7]

var = reduce(lambda x, y: 10 * x + y, lst)
print(var)
