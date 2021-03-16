# Write a program to get the sum and multiply of all the items in a given list.


a = [1, 2, 3, 4, 5]


def sumMyList(k):
    add = 0
    for i in a:
        add += i
    return add


def multiplyMyList(k1):
    mul = 1
    for i in a:
        mul *= i
    return mul


print("Sum of list is: ", sumMyList(a))
print("Multiply of list is: ", multiplyMyList(a))