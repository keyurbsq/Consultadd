print(
    "Please read and enter accordingly: \n Enter 1 for Addition, \n Enter 2 for Subtraction, \n Enter 3 for Division, \n Enter 4 for Multiplication, \n Enter 5 for Average")
userNum = int(input("Enter your selection: "))
if (userNum == 1) or (userNum == 2) or (userNum == 3) or (userNum == 4):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if userNum == 1:
        a = num1 + num2
        if a < 0:
            print("NEGATIVE")
        else:
            print(a)
    elif userNum == 2:
        a = num1 - num2
        if a < 0:
            print("NEGATIVE")
        else:
            print(a)
    elif userNum == 3:
        a = num1 / num2
        if a < 0:
            print("NEGATIVE")
        else:
            print(a)
    elif userNum == 4:
        a = num1 * num2
        if a < 0:
            print("NEGATIVE")
        else:
            print(a)
elif userNum == 5:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))
    # if userNum == 5:
    avg = (first + second) / 2
    if avg < 0:
        print("NEGATIVE")
    else:
        print(avg)