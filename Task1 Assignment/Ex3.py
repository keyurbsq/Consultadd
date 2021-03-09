#with using third variable
a = 10
b = 100
temp = b
b = a
a = temp
print(a)
print(b) 

#without using third variable
a = 10
b = 100
a,b = b,a
print(a)
print(b)