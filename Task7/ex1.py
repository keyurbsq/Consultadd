import math
C = 50
H = 30
D = input("enter number comma separated: ")
k = D.split(',')
result = []
for i in k:
    calculate = round(math.sqrt(2*C*int(i)/H))
    result.append(calculate)
print(result)