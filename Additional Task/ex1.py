#. Create a list of given structure and get the Access list as provided below:
#x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
a = []
#Access list: [1, 2, 3, 4]
print(x[5][0:4])


#Access list: [600,700]
print(x[6:8])

#Access list: [100, 300, 500, 600, 800]
print(x[0::2])

#Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])

#Access list: [10]
print(x[5][5][0])

#Access list: []
print(a)