k = input("Enter words to sort with '-' separated : ")
p = k.split("-")
p.sort()
print("-".join(p))