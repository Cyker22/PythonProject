#Random floats from 0 to 1
import numpy as np

#GENERATE random floats 3X4 array  
arr1=np.random.rand(3, 4)
print("random floats:\n",arr1)

#random intergers
arr2= np.random.randint(0, 10, size=(2,3))
print("random intergers:\n", arr2)

#normal distribution
arr3= np.random.randn(2,2)
print("random distro:\n" , arr3)

#random choice
arr4= np.random.choice([1,5,9], size=3)
print("random choice", arr4)

#shuffling arrays
arr5=np.random.seed(42) #to reproduce
arr5=np.arange(5)
np.random.shuffle(arr5) 
print("reproduce arrays\n" , arr5)

#General Example
scores = np.random.randint(0,101, size=100)
print(scores.mean(),scores.max)

