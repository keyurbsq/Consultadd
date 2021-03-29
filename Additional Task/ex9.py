# Write a program to find out the occurrence of a specific character from an alphanumeric string
k = "12abcbacbaba344ab"
a = list(k)
alpha = []

for i in a:
    if i not in alpha:
        if i.isalpha():
            alpha.append(i)
            c = 0
            for j in range(len(a)):
                if i == a[j]:
                    c += 1
            print("{} = {}".format(i, c))
