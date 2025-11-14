##Numerical Python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array)

print(type(array))

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)

#how many dimensions
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#index
array = np.array([1, 2, 3, 4])
print(array[2] + array[3])

array = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', array[1, 4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 1])

##negative index
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -2])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

print(arr[4:])

print(arr[:4])

print(arr[-3:-1])

print(arr[1:5:2])

print(arr[::2]) 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

print(arr[0:2, 1:4])

##data type
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i8')
print(arr)
print(arr.dtype)

