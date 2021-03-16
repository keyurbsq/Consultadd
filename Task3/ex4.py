# Find the largest and smallest number from a given list.

a = [1, 2, 3, 4, 5, 4, 10, 100, 20003, 200, 12, -9, -100, -124, 90]


def Large(p):
    large = a[0]
    for i in a:
        if i > large:
            large = i
    return large


print("Largest element in list is: ", Large(a))


def Small(p):
    small = a[0]
    for i in a:
        if i < small:
            small = i
    return small


print("Smallest element in list is: ", Small(a))


