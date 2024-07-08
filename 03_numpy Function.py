import numpy as np

a = np.array([
    [1,2,3,12],
    [4,5,6,12],
    [7,8,9,12]
])
b = np.array([
    [1,2,3,12],
    [4,5,6,12],
    [7,8,9,12]
])
# print(np.sin(a))
# print(np.cos(a))
# print(np.tan(a))
# print(np.exp(a)) #e^1 
# print(np.sqrt(a)) 
# print(np.square(a)) 
# print(a.sum())
# print(a.max())
# print(a.min())
# print(a.mean())
# print(np.median(a))  #middle value
# print(np.std(a))   #standard deviation
# a = a.reshape((2,6))
# print(a)

# mat = [[1,2],[3,4]]
# a = np.array(mat)
# x = a.reshape((1,4))  #(2,3,4)
# print(x)

# print(a.flatten())  #convert in 1D

# print(a.transpose()) # 4X3 -> 3X4
# print(a.flat[7])  #pos
# c = np.concatenate((a,b))
# print(c)

# c1= np.stack((a,b)) # shape (2,3,4)
# c1= np.hstack((a,b))                  [[ 1  2  3 12  1  2  3 12]
                                    #   [ 4  5  6 12  4  5  6 12]
                                    #   [ 7  8  9 12  7  8  9 12]]
# c1= np.vstack((a,b))
# [[ 1  2  3 12]
#  [ 4  5  6 12]
#  [ 7  8  9 12]
#  [ 1  2  3 12]
#  [ 4  5  6 12]
#  [ 7  8  9 12]]
# print(c1)

print(np.split(a,3))
# [array([[ 1,  2,  3, 12]]), array([[ 4,  5,  6, 12]]), array([[ 7,  8,  9, 12]])]

print(np.hsplit(a,2))
# [array([[1, 2],
#        [4, 5],
#        [7, 8]]), array([[ 3, 12],
#        [ 6, 12],
#        [ 9, 12]])]

c = [1,2,3,5]

print(np.append(a,[c],axis=0))
# [[ 1  2  3 12]
#  [ 4  5  6 12]
#  [ 7  8  9 12]
#  [ 1  2  3  5]]

print(np.insert(a,1,c,axis=0))
# [[ 1  2  3 12]
#  [ 1  2  3  5]
#  [ 4  5  6 12]
#  [ 7  8  9 12]]
