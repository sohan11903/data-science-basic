import numpy as np

# a = np.array([[1,2,3,4],[5,6,7,8]])
# b = np.array([[5,6,7,8],[1,2,3,4]])
# print(a*b)
# print(a+b)
# print(b[1])

# a=np.zeros((3,5,3)) #5 = total output 7 = row 3 = cols 
# a=np.full((3,5,3), 1) #5 = total output 7 = row 3 = cols 1 = fill the matrix with 1
# a=np.empty((2,3,3)) #fill with garbage value
# a=np.random.random((2,3,3)) #fill with random val
# print(a)

# x = np.array([0,5,10,15,20,25,30])
# y = x*2 - x ** 2
# print(y)

# x=np.arange(0,35,5)
# y= x*2 - x**2
# print(y)

# y=np.sin(x)
# print(y)

x= np.linspace(0,30,5) #equall part of the 0-30  0, 7.5, 15, 22.5, 30
print(x)

a = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [1,2,3],
        [4,5,6],
        # [2,1]   #give (2,)
    ]
],#dtype=float
)
print(a.shape)  #(2,2,3)
print(a.size)  #12
print(a.ndim) #3
print(a.dtype) #int 32