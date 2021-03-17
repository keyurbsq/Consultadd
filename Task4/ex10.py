k = range(1, 21)
oddResults = filter(lambda x: x % 2 != 0, k) #For odd
print("Odd list ", list(oddResults))
evenResults = filter(lambda x: x % 2 == 0, k) #For even
print("Even list",list(evenResults))