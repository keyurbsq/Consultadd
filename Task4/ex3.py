def uniqueList(lst):
    x = []
    for i in lst:
        if i not in x:
            x.append(i)
    return x


print(uniqueList([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))