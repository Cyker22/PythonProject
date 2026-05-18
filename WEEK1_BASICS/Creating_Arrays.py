import numpy as np

arr1 = np.arange(1,11) #numbers from 1-10
print(arr1)

#array of even numbers from 2-20
arr2 = np.arange(2,21,2)

print(arr2) #should print all even ffom[2,4....20]

#3x3 Matrix Filled with zeros
arr3 = np.zeros((3,3))
print(arr3)

#4x4 matrix filled with ones 
arr4= np.ones((4,4))
print (arr4)

#identity Matrix 5x5
arr5 =np.eye(5)
print(arr5)

#Array containing Multiples of 5 up to 100
arr6 = np.arange(5,101,5)
print(arr6)
