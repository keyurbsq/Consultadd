"""
 Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits” 

"""


k = int(input("Enter 4 digit number: "))
convert = str(k)
l = len(convert)

while l != 4:
    try:
        k = input("The length is too short/long !!! Please provide only four digits ")
        l = len(k)
    except ValueError:
        print("Value Error")
