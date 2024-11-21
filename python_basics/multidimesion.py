from numpy import *
arr1 = array([
              [3,5,8,9,4,1],
              [55,98,7,2,6,55]
              ])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.size)
print(arr1.shape, end=' = number od rows and colums')
print()

arr2 = arr1.reshape(2,2,3)
print(arr2)

print(arr2.flatten())

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('1 2 3; 4 5 6; 7 8 9')
print("m==","\n",m1*m2)
print("-----------------------------\n")
print(m1.diagonal())