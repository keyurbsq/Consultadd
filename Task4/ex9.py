def showNumbers(userNum):
    k = range(0,  userNum + 1)
    for i in k:
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD ")


a = int(input("enter number: "))
showNumbers(a)
