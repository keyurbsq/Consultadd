#Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length.

k = 'hello my name is abcde'
p = k.split(" ")
print(p)
for i in p:
    if len(i) % 2 == 0:
        print(i)
