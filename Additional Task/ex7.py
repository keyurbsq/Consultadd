#7. Write a program in python to print the pair of numbers whose sum is equal to the result
#number that is let's say 8.


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
s = 8
for i in x:
    for j in x:
        if i + j == s:
            print(i, j)