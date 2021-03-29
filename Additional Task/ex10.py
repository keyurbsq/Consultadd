#Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
p = []
for i in a:
    if i % 2 == 0:
        p.append(i)
k = tuple(p)
print(k)