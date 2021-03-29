#Write a program in Python to reverse a string and print only the vowel alphabet if it exists  in the
#string with their index

string with their index
k = "keyur"[::-1]
vowel = ["a","e","i","o","u"]

for i in k:
    if i in vowel:
        print(i, k.index(i))
       