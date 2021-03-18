# Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst))))
