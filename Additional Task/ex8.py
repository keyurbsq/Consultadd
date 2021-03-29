"""
Write a program in Python to complete the following taskCreate two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
Keep that in mind you can only add 5 items in each list
Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list.
"""


even_list = []
old_list = []
evenSum = 0
oddSum = 0
 
k = (input("Enter number from 1 - 50: "))
a = k.split()

for i in a:
    i = int(i)
    if i % 2 == 0:
        evenSum += i
        even_list.append(i)
    else:
        oddSum += i
        old_list.append(i)


print("odd list: ", old_list)
print("even list: ", even_list)
print("old sum: ", oddSum)
print("even sum: ", evenSum)
print("maximum of the odd list: ", max(old_list))
print("maximum of the even list: ", max(even_list))