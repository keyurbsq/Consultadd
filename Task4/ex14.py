#Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.Make sure to use only higher order functions.
k = int(input("enter number: "))
x = filter(lambda x: x % 3 != 0 and x % 7 != 0, range(1, k + 1))
print(list(x))