#checking properties of array a=np.arrray([[1,2,3],[4,5,6]]).

import numpy as np

a= np.array([[1,2,3],[4,5,6]])

#Finding each property by line 
print("shape:", a.shape)
print("size", a.size)
print("dimension", a.ndim)
print("Datatype", a.dtype)

#converting datatype to float
a_float = a.astype(float)
print(a_float)
print("new Datatype:", a_float.dtype)

#Reshaping The array into 3x3
a_reshaped =a.reshape(3,2)
print(a_reshaped)

#we can olny reshape Arrays 
# with the same total size like 3x2=6 but 3x3=9 
# would give an erorr

