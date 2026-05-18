#here we change the shapes of array without changging the data

import numpy as np
arr=np.arange(1,13)
print(arr.shape)

#2D 3x4 array
mat=arr.reshape(3,4)
print(mat)

#3D 2x2x3 array
tensor=arr.reshape(2,2,3)
print(tensor.shape)

#for numpy to identify on its own
arr.reshape(3,-1)  #3x4 automatically

arr.reshape(-1,4) #3x4
print (arr)