"""Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.
"""

import sys
f = sys.argv[1]
while True:
    try:
        file = open(f, 'r')
        content = file.readline()
        print(content)
        file.close()
        break
    except IOError:
        reenter = input("Invalid Name, enter Y to reenter file name ")
        if reenter =="Y":
            f = input("enter valid file name: ")
        else:
            break