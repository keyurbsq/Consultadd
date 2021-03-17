def fun():
    a1 = range(1, 21)
    k = []
    for i in a1:
        a = i * i
        k.append(a)
    return tuple(k)


print(fun())
