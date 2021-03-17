def fun(a, b):
    ke = len(a)
    ky = len(b)
    if ke == ky:
        print(a)
        print(b)
    elif ke > ky:
        print(a)
    elif ky > ke:
        print(b)


k = input("Enter first string: ")
e = input("Enter second string: ")
fun(k, e)
